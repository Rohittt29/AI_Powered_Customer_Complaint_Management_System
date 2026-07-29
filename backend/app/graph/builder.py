from langgraph.graph import StateGraph, END
from app.graph.state import ComplaintState
from app.graph.nodes import (
    entry_node, intent_router_node, complaint_parser_node,
    document_extraction_node, complaint_edit_node, validation_node,
    risk_assessment_node, response_generation_node, commit_node, end_node
)
from app.graph.router import route_after_intent, route_after_validation
from app.graph.checkpoint import get_checkpointer

def build_graph():
    """
    Assembles the entire LangGraph workflow.
    Uses LangGraph best practices to define nodes, edges, and conditional routing.
    """
    # Initialize StateGraph with our Pydantic schema
    # Note: Using Pydantic models directly as state schema is supported in LangGraph.
    workflow = StateGraph(ComplaintState)

    # Add Nodes
    workflow.add_node("entry_node", entry_node)
    workflow.add_node("intent_router_node", intent_router_node)
    workflow.add_node("complaint_parser_node", complaint_parser_node)
    workflow.add_node("document_extraction_node", document_extraction_node)
    workflow.add_node("complaint_edit_node", complaint_edit_node)
    workflow.add_node("validation_node", validation_node)
    workflow.add_node("risk_assessment_node", risk_assessment_node)
    workflow.add_node("response_generation_node", response_generation_node)
    workflow.add_node("commit_node", commit_node)
    workflow.add_node("end_node", end_node)

    # Set Entry Point
    workflow.set_entry_point("entry_node")
    
    # Sequential transition to intent router
    workflow.add_edge("entry_node", "intent_router_node")

    # Conditional branching from intent router based on UserIntent
    workflow.add_conditional_edges(
        "intent_router_node",
        route_after_intent,
        {
            "complaint_parser_node": "complaint_parser_node",
            "complaint_edit_node": "complaint_edit_node",
            "document_extraction_node": "document_extraction_node",
            "validation_node": "validation_node",
            "commit_node": "commit_node",
            "response_generation_node": "response_generation_node",
        }
    )

    # Converge execution paths to validation node
    workflow.add_edge("complaint_parser_node", "validation_node")
    workflow.add_edge("document_extraction_node", "validation_node")
    workflow.add_edge("complaint_edit_node", "validation_node")

    # Conditional branching from validation based on correctness
    workflow.add_conditional_edges(
        "validation_node",
        route_after_validation,
        {
            "risk_assessment_node": "risk_assessment_node",
            "response_generation_node": "response_generation_node"
        }
    )

    # Sequential execution after risk assessment
    workflow.add_edge("risk_assessment_node", "response_generation_node")
    
    # Finalize execution paths
    workflow.add_edge("response_generation_node", "end_node")
    workflow.add_edge("commit_node", "end_node")
    workflow.add_edge("end_node", END)

    # Compile the graph with the in-memory checkpointer
    checkpointer = get_checkpointer()
    return workflow.compile(checkpointer=checkpointer)
