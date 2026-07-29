from app.agents.base_agent import BaseAgent
from app.graph.state import ComplaintState

class DocumentExtractionAgent(BaseAgent):
    """
    Agent responsible for converting raw OCR text into structured 
    complaint information.
    """
    
    @property
    def agent_name(self) -> str:
        return "DocumentExtractionAgent"
        
    @property
    def description(self) -> str:
        return "Converts extracted document text into structured complaint information."

    async def _execute(self, state: ComplaintState) -> ComplaintState:
        """
        TODO: Implement Document Extraction LLM parsing.
        - Read OCR text from state.uploaded_documents.
        - Merge extracted information into ComplaintState.
        (Note: Does NOT implement OCR itself, only consumes the text).
        """
        self.logger.info(f"[{self.agent_name}] Extracting data from document text...")
        
        # Placeholder update
        # if state.uploaded_documents:
        #    process_text(state.uploaded_documents[-1].extracted_text)
            
        return state
