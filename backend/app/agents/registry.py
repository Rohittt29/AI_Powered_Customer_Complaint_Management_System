from app.agents.base_agent import BaseAgent
from app.agents.intake_agent import ComplaintIntakeAgent
from app.agents.parser_agent import ComplaintParsingAgent
from app.agents.validation_agent import ComplaintValidationAgent
from app.agents.edit_agent import ComplaintEditAgent
from app.agents.document_agent import DocumentExtractionAgent
from app.agents.risk_agent import RiskAssessmentAgent
from app.agents.commit_agent import QMSCommitAgent
from app.agents.response_agent import ResponseGenerationAgent

class AgentRegistry:
    """
    Central registry for all AI agents.
    Supports easy retrieval and future dependency injection.
    """
    
    def __init__(self):
        self._agents = {
            "intake": ComplaintIntakeAgent(),
            "parser": ComplaintParsingAgent(),
            "validation": ComplaintValidationAgent(),
            "edit": ComplaintEditAgent(),
            "document": DocumentExtractionAgent(),
            "risk": RiskAssessmentAgent(),
            "commit": QMSCommitAgent(),
            "response": ResponseGenerationAgent(),
        }
        
    def get_agent(self, name: str) -> BaseAgent:
        """
        Retrieve an agent by its short name.
        """
        if name not in self._agents:
            raise ValueError(f"Agent '{name}' not found in registry.")
        return self._agents[name]
        
    def list_agents(self) -> list[str]:
        """
        List all registered agent names.
        """
        return list(self._agents.keys())

# Global registry instance
agent_registry = AgentRegistry()
