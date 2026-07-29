from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import date, datetime
from uuid import UUID

from app.schemas.common import ComplaintStatus
from app.schemas.customer import CustomerResponse, CustomerCreate
from app.schemas.product import ProductResponse, ProductCreate
from app.schemas.document import UploadedDocumentResponse
from app.schemas.risk import RiskAssessmentResponse
from app.schemas.common import ValidationResponse

class ComplaintDetailsBase(BaseModel):
    """Base schema for specific complaint operational details"""
    defect_type: Optional[str] = Field(None, max_length=100)
    quantity_affected: Optional[int] = Field(None, ge=0, description="Cannot be negative")
    issue_description: Optional[str] = None
    observed_date: Optional[date] = None
    location: Optional[str] = Field(None, max_length=255)

class ComplaintDetailsCreate(ComplaintDetailsBase):
    """Schema for creating complaint details"""
    pass

class ComplaintBase(BaseModel):
    """Base schema for the core complaint entity"""
    complaint_description: str = Field(..., min_length=1, description="Description cannot be empty")
    complaint_category: Optional[str] = Field(None, max_length=100)
    complaint_source: Optional[str] = Field(None, max_length=100)
    complaint_date: Optional[date] = Field(None, description="Cannot be in the future")

class ComplaintCreate(ComplaintBase):
    """Schema for creating a new complaint"""
    customer: Optional[CustomerCreate] = None
    product: Optional[ProductCreate] = None
    details: Optional[ComplaintDetailsCreate] = None

class ComplaintUpdate(BaseModel):
    """Schema for updating an existing complaint (conversational or manual)"""
    complaint_description: Optional[str] = Field(None, min_length=1)
    complaint_category: Optional[str] = Field(None, max_length=100)
    complaint_source: Optional[str] = Field(None, max_length=100)
    complaint_date: Optional[date] = None
    complaint_status: Optional[ComplaintStatus] = None

class ComplaintResponse(ComplaintBase):
    """Schema for returning full complaint information"""
    complaint_id: UUID
    complaint_number: str
    complaint_status: ComplaintStatus
    created_at: datetime
    updated_at: datetime
    
    # Relationships
    customer: Optional[CustomerResponse] = None
    product: Optional[ProductResponse] = None
    details: Optional[ComplaintDetailsBase] = None
    documents: List[UploadedDocumentResponse] = Field(default_factory=list)
    risk_assessment: Optional[RiskAssessmentResponse] = None
    validation_result: Optional[ValidationResponse] = None

    model_config = ConfigDict(from_attributes=True)

class ComplaintListResponse(BaseModel):
    """Schema for returning a summarized list of complaints"""
    complaint_id: UUID
    complaint_number: str
    complaint_date: Optional[date]
    complaint_status: ComplaintStatus
    complaint_category: Optional[str]
    customer_name: Optional[str] = None
    product_name: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
