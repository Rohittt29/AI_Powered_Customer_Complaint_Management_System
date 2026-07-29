import os
from pydantic_settings import BaseSettings

class LLMSettings(BaseSettings):
    """
    Configuration for LLM Providers.
    Values are loaded from .env automatically.
    """
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "dummy_key_for_now")
    GROQ_MODEL_NAME: str = os.getenv("GROQ_MODEL_NAME", "gemma2-9b-it")
    LLM_TEMPERATURE: float = 0.0
    LLM_MAX_RETRIES: int = 3
    LLM_TIMEOUT_SECONDS: int = 30

    class Config:
        env_file = ".env"

llm_settings = LLMSettings()
