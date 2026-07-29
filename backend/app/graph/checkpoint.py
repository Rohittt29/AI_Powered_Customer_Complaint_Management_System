from langgraph.checkpoint.memory import MemorySaver

# Use an in-memory checkpoint implementation for now.
# Database persistence will be added later in subsequent modules.
memory_saver = MemorySaver()

def get_checkpointer():
    """
    Provides the checkpointer for state persistence, workflow recovery, 
    and session continuity.
    """
    return memory_saver
