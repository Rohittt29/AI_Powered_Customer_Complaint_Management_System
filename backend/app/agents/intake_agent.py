from app.agents.base_agent import BaseAgent
from app.graph.state import ComplaintState

class ComplaintIntakeAgent(BaseAgent):
    """
    Agent responsible for receiving initial user inputs and normalizing them.
    Does not perform extraction or routing logic itself.
    """
    
    @property
    def agent_name(self) -> str:
        return "ComplaintIntakeAgent"
        
    @property
    def description(self) -> str:
        return "Receives new complaint requests, initializes state, and normalizes input."

    async def _execute(self, state: ComplaintState) -> ComplaintState:
        """
        TODO: Implement AI logic.
        - Normalize initial user input.
        - Prepare data for parsing.
        """
        self.logger.info(f"[{self.agent_name}] Normalizing user input: {state.session_info.current_user_prompt}")
        
        # Placeholder update
        # state.metadata["normalized_input"] = "..."
        
        return state
