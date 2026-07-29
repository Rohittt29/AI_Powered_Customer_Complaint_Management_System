from app.tools.base_tool import BaseTool
from app.tools.complaint_extractor import ComplaintExtractionTool
from app.tools.complaint_updater import ComplaintUpdateTool
from app.tools.validator import ComplaintValidationTool
from app.tools.document_extractor import DocumentExtractionTool
from app.tools.ocr_tool import OCRTool
from app.tools.risk_tool import RiskAssessmentTool
from app.tools.intent_classifier import IntentClassificationTool
from app.tools.persistence_tool import DatabasePersistenceTool
from app.tools.response_formatter import ResponseFormattingTool

class ToolRegistry:
    """
    Central registry for all deterministic and AI-assisted tools.
    Supports easy retrieval and future dependency injection.
    """
    
    def __init__(self):
        self._tools = {
            "complaint_extractor": ComplaintExtractionTool(),
            "complaint_updater": ComplaintUpdateTool(),
            "validator": ComplaintValidationTool(),
            "document_extractor": DocumentExtractionTool(),
            "ocr": OCRTool(),
            "risk": RiskAssessmentTool(),
            "intent_classifier": IntentClassificationTool(),
            "persistence": DatabasePersistenceTool(),
            "response_formatter": ResponseFormattingTool(),
        }
        
    def get_tool(self, name: str) -> BaseTool:
        """
        Retrieve a tool by its short name.
        """
        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found in registry.")
        return self._tools[name]
        
    def list_tools(self) -> list[str]:
        """
        List all registered tool names.
        """
        return list(self._tools.keys())

# Global registry instance
tool_registry = ToolRegistry()
