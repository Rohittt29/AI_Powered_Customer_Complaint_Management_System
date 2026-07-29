"""
Security Middleware.
Implements rate limiting, secure response headers, and request size limiting
for production hardening.
"""
import time
import logging
from collections import defaultdict
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

logger = logging.getLogger("app.security")

# Simple in-memory rate limiter (per-IP, per-minute)
_rate_store: dict = defaultdict(list)
RATE_LIMIT = 100  # requests per minute per IP
RATE_WINDOW = 60  # seconds
MAX_REQUEST_SIZE = 10 * 1024 * 1024  # 10 MB


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Injects security headers into every response."""

    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"

        return response


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Simple in-memory rate limiter. Swap with Redis for distributed deployments."""

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "unknown"
        now = time.time()

        # Clean old entries
        _rate_store[client_ip] = [
            ts for ts in _rate_store[client_ip] if now - ts < RATE_WINDOW
        ]

        if len(_rate_store[client_ip]) >= RATE_LIMIT:
            logger.warning(f"Rate limit exceeded for IP: {client_ip}")
            return JSONResponse(
                status_code=429,
                content={"success": False, "error": {"code": "RATE_LIMITED", "message": "Too many requests. Please try again later."}},
            )

        _rate_store[client_ip].append(now)
        return await call_next(request)


class RequestSizeLimitMiddleware(BaseHTTPMiddleware):
    """Rejects requests with bodies larger than MAX_REQUEST_SIZE."""

    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > MAX_REQUEST_SIZE:
            return JSONResponse(
                status_code=413,
                content={"success": False, "error": {"code": "PAYLOAD_TOO_LARGE", "message": "Request body exceeds 10MB limit."}},
            )
        return await call_next(request)
