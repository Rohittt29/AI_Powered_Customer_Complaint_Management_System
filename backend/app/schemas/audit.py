from typing import Any, Dict, Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from uuid import UUID

class AuditLogBase(BaseModel):
    """Base schema for audit logging"""
    entity_type: str = Field(..., max_length=100)
    entity_id: UUID
    action: str = Field(..., max_length=100)
    performed_by: str = Field(default="system", max_length=100)
    previous_value: Optional[Dict[str, Any]] = None
    new_value: Optional[Dict[str, Any]] = None

class AuditLogCreate(AuditLogBase):
    """Schema for creating an audit log"""
    pass

class AuditLogResponse(AuditLogBase):
    """Schema for returning an audit log"""
    audit_id: UUID
    performed_at: datetime

    model_config = ConfigDict(from_attributes=True)
