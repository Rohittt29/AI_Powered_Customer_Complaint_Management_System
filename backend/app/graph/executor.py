import logging
from app.graph.state import ComplaintState, WorkflowStage
from app.graph.builder import build_graph

logger = logging.getLogger(__name__)

class GraphExecutor:
    """
    Orchestrates the execution of the LangGraph workflow.
    """
    def __init__(self):
        self.app = build_graph()

    async def execute(self, state: ComplaintState) -> ComplaintState:
        """
        Receives ComplaintState, executes the graph, and returns final ComplaintState.
        Implements graceful error handling.
        """
        logger.info(f"[Executor] Starting execution for session: {state.session_id}")
        config = {"configurable": {"thread_id": state.session_id}}
        
        try:
            # Execute the LangGraph workflow. 
            # `ainvoke` passes the state through the graph and returns the final state dict.
            result_dict = await self.app.ainvoke(state.model_dump(), config=config)
            
            logger.info(f"[Executor] Execution completed successfully for session: {state.session_id}")
            return ComplaintState(**result_dict)
            
        except Exception as e:
            logger.error(f"[Executor] Error during graph execution: {e}")
            
            # Graceful error handling: preserve state, update error fields
            state.errors.append(str(e))
            state.current_workflow_stage = WorkflowStage.ERROR
            
            return state

# Global executor instance
executor = GraphExecutor()
