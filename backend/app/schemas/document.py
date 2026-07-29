from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from uuid import UUID

from app.schemas.common import ExtractionStatus

class UploadedDocumentBase(BaseModel):
    """Base schema for document properties"""
    file_name: str = Field(..., max_length=255)
    file_type: str = Field(..., max_length=50)
    file_size: int = Field(..., ge=0, description="Size of file in bytes")
    storage_path: str = Field(..., max_length=1024)
    extraction_status: ExtractionStatus = Field(default=ExtractionStatus.PENDING)
    extracted_text: Optional[str] = None

class UploadedDocumentCreate(UploadedDocumentBase):
    """Schema for creating a document record"""
    pass

class UploadedDocumentResponse(UploadedDocumentBase):
    """Schema for returning document information"""
    document_id: UUID
    upload_time: datetime
    complaint_id: UUID

    model_config = ConfigDict(from_attributes=True)
