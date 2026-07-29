from app.tools.base_tool import BaseTool

class OCRTool(BaseTool):
    """
    Tool for Optical Character Recognition processing.
    """
    
    @property
    def tool_name(self) -> str:
        return "OCRTool"
        
    @property
    def description(self) -> str:
        return "Extracts machine-readable text from uploaded complaint documents."

    async def _execute(self, file_path: str) -> str:
        """
        TODO: Implement OCR engine integration.
        - Accept uploaded files.
        - Return extracted text.
        """
        self.logger.info(f"Performing OCR on {file_path}...")
        
        # Placeholder implementation
        return "Extracted raw text placeholder."
