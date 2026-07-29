from abc import ABC, abstractmethod
from typing import Type, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class LLMProvider(ABC):
    """
    Abstract interface for LLM Providers.
    Ensures future models are swappable without changing business logic.
    """
    
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate unstructured text from a prompt."""
        pass
        
    @abstractmethod
    async def generate_json(self, prompt: str, schema: Type[T]) -> T:
        """Generate structured JSON adhering to a Pydantic schema."""
        pass
