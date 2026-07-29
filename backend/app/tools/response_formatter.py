from app.tools.base_tool import BaseTool
from app.schemas.state import ComplaintState

class ResponseFormattingTool(BaseTool):
    """
    Tool to generate frontend-friendly AI Copilot conversational messages.
    """
    
    @property
    def tool_name(self) -> str:
        return "ResponseFormattingTool"
        
    @property
    def description(self) -> str:
        return "Converts internal workflow results into a clear, concise AI response."

    async def _execute(self, state: ComplaintState) -> str:
        """
        TODO: Implement LLM formatting logic.
        - Convert ComplaintState into frontend response.
        """
        self.logger.info("Formatting conversational response...")
        
        # Placeholder implementation
        return "Workflow completed. The complaint form has been updated."
