import logging
import time
from abc import ABC, abstractmethod
from typing import Any

class BaseTool(ABC):
    """
    Abstract base class for all tools in the system.
    Enforces a strict contract for execution, validation, logging, and error handling.
    """
    
    @property
    @abstractmethod
    def tool_name(self) -> str:
        """Return the unique name of the tool."""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """Return a brief description of the tool's responsibility."""
        pass
        
    def __init__(self):
        self.logger = logging.getLogger(f"app.tools.{self.tool_name.replace(' ', '')}")
        
    def validate_input(self, **kwargs) -> bool:
        """
        Validate tool inputs before execution.
        Override in subclasses to enforce specific preconditions.
        """
        return True
        
    def validate_output(self, result: Any) -> bool:
        """
        Validate tool outputs after execution.
        Override in subclasses to enforce specific postconditions.
        """
        return True
        
    @abstractmethod
    async def _execute(self, **kwargs) -> Any:
        """
        Internal execution logic. Must be implemented by subclasses.
        DO NOT call this method directly; call `execute()` instead.
        """
        pass
        
    async def execute(self, **kwargs) -> Any:
        """
        Standard execution wrapper that provides consistent logging, timing,
        input/output validation, and graceful exception handling.
        """
        self.logger.info(f"[{self.tool_name}] Tool started.")
        start_time = time.time()
        
        try:
            # 1. Input Validation
            if not self.validate_input(**kwargs):
                raise ValueError(f"Input validation failed for {self.tool_name}")
                
            # 2. Execution
            result = await self._execute(**kwargs)
            
            # 3. Output Validation
            if not self.validate_output(result):
                raise ValueError(f"Output validation failed for {self.tool_name}")
                
            return result
            
        except Exception as e:
            self.logger.error(f"[{self.tool_name}] Error during execution: {str(e)}")
            # Return structured error dict to prevent crashing the workflow
            return {"error": True, "message": str(e), "source": self.tool_name}
            
        finally:
            duration = time.time() - start_time
            self.logger.info(f"[{self.tool_name}] Tool finished. Execution time: {duration:.2f}s")
