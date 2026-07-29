import logging
import time
from typing import Type, TypeVar
from pydantic import BaseModel

# Note: In a real environment, `langchain_groq` must be installed.
# We import defensively or mock it for the foundation phase.
try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None

from app.llm.provider import LLMProvider
from app.llm.config import llm_settings

logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseModel)

class GroqClient(LLMProvider):
    """
    Concrete implementation of the LLMProvider using Groq and LangChain.
    Handles API keys, timeouts, retries, and structured JSON parsing.
    """
    def __init__(self):
        if not ChatGroq:
            logger.warning("langchain_groq is not installed. Using placeholder LLM client.")
            self.llm = None
        else:
            self.llm = ChatGroq(
                api_key=llm_settings.GROQ_API_KEY,
                model_name=llm_settings.GROQ_MODEL_NAME,
                temperature=llm_settings.LLM_TEMPERATURE,
                max_retries=llm_settings.LLM_MAX_RETRIES,
                timeout=llm_settings.LLM_TIMEOUT_SECONDS
            )

    async def generate(self, prompt: str) -> str:
        """Generate raw text response with retry and error handling."""
        start_time = time.time()
        try:
            logger.info(f"Generating text using {llm_settings.GROQ_MODEL_NAME}...")
            
            if self.llm is None:
                return "Placeholder LLM Response"
                
            response = await self.llm.ainvoke(prompt)
            return response.content
            
        except Exception as e:
            logger.error(f"LLM API failure during text generation: {e}")
            raise
        finally:
            duration = time.time() - start_time
            logger.info(f"LLM execution time: {duration:.2f}s")

    async def generate_json(self, prompt: str, schema: Type[T]) -> T:
        """Generate structured JSON response using LangChain's structured output."""
        start_time = time.time()
        try:
            logger.info(f"Generating JSON using {llm_settings.GROQ_MODEL_NAME} for schema {schema.__name__}...")
            
            if self.llm is None:
                # Fallback empty instance for placeholder
                return schema()
                
            # LangChain handles formatting instructions and JSON parsing automatically
            structured_llm = self.llm.with_structured_output(schema)
            response = await structured_llm.ainvoke(prompt)
            return response
            
        except Exception as e:
            logger.error(f"LLM API failure during JSON generation: {e}")
            raise
        finally:
            duration = time.time() - start_time
            logger.info(f"LLM execution time: {duration:.2f}s")
