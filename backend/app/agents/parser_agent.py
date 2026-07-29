from app.agents.base_agent import BaseAgent
from app.graph.state import ComplaintState
from app.schemas.complaint import ComplaintBase

class ComplaintParsingAgent(BaseAgent):
    """
    Agent responsible for converting natural language descriptions into 
    structured Pydantic schemas without fabricating information.
    """
    
    @property
    def agent_name(self) -> str:
        return "ComplaintParsingAgent"
        
    @property
    def description(self) -> str:
        return "Converts natural language into structured complaint fields."

    async def _execute(self, state: ComplaintState) -> ComplaintState:
        """
        TODO: Implement LLM parsing.
        - Invoke LangChain tool to parse state.session_info.current_user_prompt.
        - Populate state.complaint, state.product, state.customer.
        - Preserve unknown values as null.
        """
        self.logger.info(f"[{self.agent_name}] Parsing complaint data...")
        
        # Placeholder update
        if not state.complaint:
            state.complaint = ComplaintBase(
                complaint_description=state.session_info.current_user_prompt,
                complaint_category="Pending"
            )
            
        return state
