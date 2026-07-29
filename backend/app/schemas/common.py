from typing import Any, Dict, Generic, List, Optional, TypeVar
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from enum import Enum

T = TypeVar("T")

# Enums used across schemas
class ComplaintStatus(str, Enum):
    DRAFT = "Draft"
    PENDING_ASSESSMENT = "Pending Assessment"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class ExtractionStatus(str, Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"

class RiskLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class MessageSender(str, Enum):
    USER = "User"
    AI = "AI"
    SYSTEM = "System"

# Standard Response Envelopes
class GenericSuccessResponse(BaseModel, Generic[T]):
    """Standard success response envelope"""
    success: bool = True
    message: str = "Operation completed successfully."
    data: Optional[T] = None

class ErrorDetail(BaseModel):
    """Detailed error information"""
    code: str
    message: str

class ErrorResponse(BaseModel):
    """Standard error response envelope"""
    success: bool = False
    error: ErrorDetail

class ValidationResponse(BaseModel):
    """Result of a complaint validation check"""
    is_valid: bool = Field(..., description="Whether the complaint is fully valid and ready to save")
    completeness_score: int = Field(..., ge=0, le=100, description="Score from 0 to 100")
    missing_fields: List[str] = Field(default_factory=list, description="Fields that are required but missing")
    warnings: List[str] = Field(default_factory=list, description="Non-critical warnings or suspicious entries")
    validation_timestamp: datetime = Field(default_factory=datetime.utcnow)
