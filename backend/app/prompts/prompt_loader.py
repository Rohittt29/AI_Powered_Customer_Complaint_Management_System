import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class PromptLoader:
    """
    Loads prompt templates and safely injects variables.
    Keeps prompts separated from business logic.
    """
    @staticmethod
    def load(prompt_template: str, variables: Dict[str, Any]) -> str:
        """
        Injects variables into the prompt template using standard format string.
        Validates placeholders.
        """
        try:
            return prompt_template.format(**variables)
        except KeyError as e:
            logger.error(f"Missing required prompt variable: {e}")
            raise ValueError(f"Missing required prompt variable: {e}")
        except Exception as e:
            logger.error(f"Failed to load prompt: {e}")
            raise
