from app.agents.base_agent import BaseAgent
from app.graph.state import ComplaintState

class ComplaintEditAgent(BaseAgent):
    """
    Agent responsible for applying conversational updates to existing data
    without losing previously extracted information.
    """
    
    @property
    def agent_name(self) -> str:
        return "ComplaintEditAgent"
        
    @property
    def description(self) -> str:
        return "Applies specific conversational updates to existing complaint data."

    async def _execute(self, state: ComplaintState) -> ComplaintState:
        """
        TODO: Implement LLM edit reasoning.
        - Analyze user update request.
        - Update ONLY requested fields.
        - Preserve all existing data.
        - Track modified fields in metadata.
        """
        self.logger.info(f"[{self.agent_name}] Processing edit request...")
        
        # Placeholder update
        # state.metadata["last_edit"] = "..."
            
        return state
