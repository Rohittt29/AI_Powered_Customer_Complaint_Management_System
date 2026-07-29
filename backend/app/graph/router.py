import logging
from app.graph.state import ComplaintState, UserIntent

logger = logging.getLogger(__name__)

def route_after_intent(state: ComplaintState) -> str:
    """
    Conditional routing based on detected user intent.
    Determines execution path without performing business logic.
    """
    intent = state.current_intent
    logger.info(f"[Router] Routing based on intent: {intent}")
    
    if intent == UserIntent.NEW_COMPLAINT:
        return "complaint_parser_node"
    elif intent == UserIntent.EDIT_COMPLAINT:
        return "complaint_edit_node"
    elif intent == UserIntent.DOCUMENT_UPLOAD:
        return "document_extraction_node"
    elif intent == UserIntent.SAVE_REQUEST:
        return "commit_node"
    elif intent == UserIntent.GENERAL_QUERY:
        return "response_generation_node"
    elif intent == UserIntent.RISK_REQUEST:
        return "validation_node"  # Validation precedes risk assessment
    
    # Default fallback
    logger.warning("[Router] Unrecognized intent, falling back to response_generation_node")
    return "response_generation_node"

def route_after_validation(state: ComplaintState) -> str:
    """
    Routes based on validation success.
    If valid, proceed to Risk Assessment. If not, return feedback via Response Generator.
    """
    # TODO: Evaluate state.validation_status.is_valid
    is_valid = True # Placeholder
    
    logger.info(f"[Router] Routing after validation. Is valid: {is_valid}")
    if is_valid:
        return "risk_assessment_node"
    else:
        return "response_generation_node"
