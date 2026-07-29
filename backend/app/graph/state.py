from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from enum import Enum

from app.schemas.complaint import ComplaintBase, ComplaintDetailsBase
from app.schemas.customer import CustomerBase
from app.schemas.product import ProductBase
from app.schemas.document import UploadedDocumentBase
from app.schemas.risk import RiskAssessmentBase
from app.schemas.common import ValidationResponse
from app.schemas.conversation import ConversationMessageBase

class WorkflowStage(str, Enum):
    NEW = "NEW"
    UNDERSTANDING = "UNDERSTANDING"
    STRUCTURED = "STRUCTURED"
    VALIDATED = "VALIDATED"
    RISK_ANALYZED = "RISK_ANALYZED"
    READY_TO_SAVE = "READY_TO_SAVE"
    SAVED = "SAVED"
    ERROR = "ERROR"

class UserIntent(str, Enum):
    NEW_COMPLAINT = "NEW_COMPLAINT"
    EDIT_COMPLAINT = "EDIT_COMPLAINT"
    DOCUMENT_UPLOAD = "DOCUMENT_UPLOAD"
    RISK_REQUEST = "RISK_REQUEST"
    SAVE_REQUEST = "SAVE_REQUEST"
    GENERAL_QUERY = "GENERAL_QUERY"

class ComplaintState(BaseModel):
    """
    The master state object passed between LangGraph nodes.
    Acts as the single source of truth during AI orchestration.
    """
    session_id: str
    complaint: Optional[ComplaintBase] = None
    customer: Optional[CustomerBase] = None
    product: Optional[ProductBase] = None
    complaint_details: Optional[ComplaintDetailsBase] = None
    uploaded_documents: List[UploadedDocumentBase] = Field(default_factory=list)
    validation_status: Optional[ValidationResponse] = None
    risk_assessment: Optional[RiskAssessmentBase] = None
    conversation_history: List[ConversationMessageBase] = Field(default_factory=list)
    
    current_workflow_stage: WorkflowStage = WorkflowStage.NEW
    current_intent: Optional[UserIntent] = None
    
    errors: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamps: Dict[str, str] = Field(default_factory=dict)
