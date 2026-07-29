from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from uuid import UUID

from app.schemas.common import RiskLevel

class RiskAssessmentBase(BaseModel):
    """Base schema for AI-generated risk assessment"""
    severity: RiskLevel
    probability: RiskLevel
    overall_risk: RiskLevel
    recommended_actions: List[str] = Field(default_factory=list)
    suggested_investigation: Optional[str] = None
    ai_reasoning: str

class RiskAssessmentCreate(RiskAssessmentBase):
    """Schema for creating a risk assessment"""
    pass

class RiskAssessmentResponse(RiskAssessmentBase):
    """Schema for returning a risk assessment"""
    risk_id: UUID
    complaint_id: UUID
    generated_at: datetime

    model_config = ConfigDict(from_attributes=True)
