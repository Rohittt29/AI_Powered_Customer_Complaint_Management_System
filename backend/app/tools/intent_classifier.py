from app.tools.base_tool import BaseTool
from app.graph.state import UserIntent

class IntentClassificationTool(BaseTool):
    """
    Tool to classify user input into a predefined workflow intent.
    """
    
    @property
    def tool_name(self) -> str:
        return "IntentClassificationTool"
        
    @property
    def description(self) -> str:
        return "Determines the user's primary intent from conversational input."

    async def _execute(self, user_prompt: str) -> UserIntent:
        """
        TODO: Implement LLM intent classification logic.
        - Analyze user_prompt.
        - Classify into one of UserIntent enums.
        """
        self.logger.info(f"Classifying intent for prompt: {user_prompt[:50]}...")
        
        # Placeholder implementation
        return UserIntent.NEW_COMPLAINT
