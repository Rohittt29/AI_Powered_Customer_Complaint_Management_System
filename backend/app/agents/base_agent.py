import logging
import time
from abc import ABC, abstractmethod
from typing import Optional

from app.graph.state import ComplaintState

class BaseAgent(ABC):
    """
    Abstract base class for all AI Agents in the system.
    Enforces a strict contract for execution, validation, logging, and error handling.
    """
    
    @property
    @abstractmethod
    def agent_name(self) -> str:
        """Return the unique name of the agent."""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """Return a brief description of the agent's responsibility."""
        pass
        
    def __init__(self):
        self.logger = logging.getLogger(f"app.agents.{self.agent_name.replace(' ', '')}")
        
    def validate_input(self, state: ComplaintState) -> bool:
        """
        Validate the input state before execution.
        Override in subclasses to enforce specific preconditions.
        """
        return True
        
    def validate_output(self, state: ComplaintState) -> bool:
        """
        Validate the output state after execution.
        Override in subclasses to enforce specific postconditions.
        """
        return True
        
    @abstractmethod
    async def _execute(self, state: ComplaintState) -> ComplaintState:
        """
        Internal execution logic. Must be implemented by subclasses.
        DO NOT call this method directly; call `execute()` instead.
        """
        pass
        
    async def execute(self, state: ComplaintState) -> ComplaintState:
        """
        Standard execution wrapper that provides consistent logging, timing,
        input/output validation, and graceful exception handling.
        """
        self.logger.info(f"[{self.agent_name}] Agent started. Session: {state.session_id}")
        start_time = time.time()
        
        try:
            # 1. Input Validation
            if not self.validate_input(state):
                raise ValueError(f"Input validation failed for {self.agent_name}")
                
            # 2. Execution
            state = await self._execute(state)
            
            # 3. Output Validation
            if not self.validate_output(state):
                raise ValueError(f"Output validation failed for {self.agent_name}")
                
        except Exception as e:
            self.logger.error(f"[{self.agent_name}] Error during execution: {str(e)}")
            # Preserve state but append error
            state.errors.append(f"{self.agent_name} Error: {str(e)}")
            # Transition to error stage gracefully
            from app.graph.state import WorkflowStage
            state.current_workflow_stage = WorkflowStage.ERROR
            
        finally:
            duration = time.time() - start_time
            self.logger.info(f"[{self.agent_name}] Agent completed. Execution time: {duration:.2f}s")
            
        return state
