from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from app.schemas.complaint import ComplaintBase, ComplaintDetailsBase
from app.schemas.customer import CustomerBase
from app.schemas.product import ProductBase
from app.schemas.document import UploadedDocumentBase
from app.schemas.risk import RiskAssessmentBase
from app.schemas.common import ValidationResponse
from app.schemas.conversation import ConversationMessageBase

class SessionInformation(BaseModel):
    """Metadata regarding the current active LangGraph session"""
    session_id: str
    conversation_id: str
    current_user_prompt: str
    timestamp: str
    active_agent: Optional[str] = None

class WorkflowMetadata(BaseModel):
    """Tracking the current execution status of the graph"""
    current_node: str
    previous_node: Optional[str] = None
    next_node: Optional[str] = None
    current_stage: str

class AuditMetadata(BaseModel):
    """Information regarding traceability of the session"""
    created_at: str
    updated_at: str
    created_by: str = "system"
    updated_by: str = "system"
    version: int = 1

class ComplaintState(BaseModel):
    """
    The master state object passed between LangGraph nodes.
    Acts as the single source of truth during AI orchestration.
    """
    session_info: SessionInformation
    complaint: Optional[ComplaintBase] = None
    customer: Optional[CustomerBase] = None
    product: Optional[ProductBase] = None
    complaint_details: Optional[ComplaintDetailsBase] = None
    uploaded_document: Optional[UploadedDocumentBase] = None
    validation_result: Optional[ValidationResponse] = None
    risk_assessment: Optional[RiskAssessmentBase] = None
    conversation_history: List[ConversationMessageBase] = Field(default_factory=list)
    workflow_metadata: WorkflowMetadata
    audit_metadata: AuditMetadata
