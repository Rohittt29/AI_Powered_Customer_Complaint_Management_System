from app.llm.provider import LLMProvider
from app.llm.client import GroqClient

class LLMFactory:
    """
    Factory to retrieve the configured LLM provider.
    Allows easy swapping of models or providers in the future.
    """
    
    @staticmethod
    def get_provider() -> LLMProvider:
        """
        Returns the primary LLM provider (Groq).
        """
        return GroqClient()

# Global provider instance
llm_provider = LLMFactory.get_provider()
