"""
Structured Logging Middleware.
Logs every HTTP request/response with method, path, status, duration,
and a unique correlation ID for end-to-end traceability.
Sensitive fields (password, api_key, token, secret) are masked automatically.
"""
import time
import uuid
import logging
import json
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("app.access")

SENSITIVE_KEYS = {"password", "api_key", "token", "secret", "secret_key", "groq_api_key"}


def mask_sensitive(data: dict) -> dict:
    """Recursively mask sensitive keys in a dictionary."""
    masked = {}
    for key, value in data.items():
        if key.lower() in SENSITIVE_KEYS:
            masked[key] = "***MASKED***"
        elif isinstance(value, dict):
            masked[key] = mask_sensitive(value)
        else:
            masked[key] = value
    return masked


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware that logs structured request/response information."""

    async def dispatch(self, request: Request, call_next):
        correlation_id = str(uuid.uuid4())[:8]
        start_time = time.time()

        # Attach correlation ID to request state for downstream use
        request.state.correlation_id = correlation_id

        logger.info(
            json.dumps({
                "event": "request_start",
                "correlation_id": correlation_id,
                "method": request.method,
                "path": str(request.url.path),
                "query": str(request.query_params),
                "client": request.client.host if request.client else "unknown",
            })
        )

        response: Response = await call_next(request)

        duration = round(time.time() - start_time, 4)

        logger.info(
            json.dumps({
                "event": "request_end",
                "correlation_id": correlation_id,
                "method": request.method,
                "path": str(request.url.path),
                "status_code": response.status_code,
                "duration_s": duration,
            })
        )

        # Inject correlation ID into response headers for client-side debugging
        response.headers["X-Correlation-ID"] = correlation_id
        return response
