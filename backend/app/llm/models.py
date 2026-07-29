from pydantic import BaseModel

class TokenUsage(BaseModel):
    """
    Model for tracking token usage if provided by the LLM response.
    """
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
