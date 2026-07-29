from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from uuid import UUID

from app.schemas.complaint import ComplaintCreate, ComplaintUpdate, ComplaintResponse, ComplaintListResponse
from app.schemas.common import GenericSuccessResponse, ErrorResponse
from app.services.complaint_service import ComplaintService
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("", response_model=GenericSuccessResponse[ComplaintResponse], status_code=status.HTTP_201_CREATED)
async def create_complaint(
    complaint_in: ComplaintCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Create a new complaint record."""
    # Delegate to service
    complaint = await ComplaintService.create_complaint(db, complaint_in)
    
    # Return placeholder until implemented
    return GenericSuccessResponse(
        success=True,
        message="Complaint created successfully.",
        data=None
    )

@router.get("", response_model=GenericSuccessResponse[List[ComplaintListResponse]])
async def list_complaints(
    status: Optional[str] = None,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Retrieve a list of complaints."""
    complaints = await ComplaintService.get_complaints(db, status=status)
    return GenericSuccessResponse(
        success=True,
        message="Complaints retrieved successfully.",
        data=complaints
    )

@router.get("/{complaint_id}", response_model=GenericSuccessResponse[ComplaintResponse])
async def get_complaint(
    complaint_id: UUID,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Retrieve a specific complaint by ID."""
    complaint = await ComplaintService.get_complaint(db, complaint_id)
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    
    return GenericSuccessResponse(
        success=True,
        message="Complaint retrieved successfully.",
        data=complaint
    )

@router.put("/{complaint_id}", response_model=GenericSuccessResponse[ComplaintResponse])
async def update_complaint(
    complaint_id: UUID,
    complaint_in: ComplaintUpdate,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Update manually edited complaint fields."""
    complaint = await ComplaintService.update_complaint(db, complaint_id, complaint_in)
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
        
    return GenericSuccessResponse(
        success=True,
        message="Complaint updated successfully.",
        data=complaint
    )

@router.delete("/{complaint_id}", response_model=GenericSuccessResponse[None])
async def delete_complaint(
    complaint_id: UUID,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Soft delete a complaint."""
    success = await ComplaintService.delete_complaint(db, complaint_id)
    if not success:
        raise HTTPException(status_code=404, detail="Complaint not found")
        
    return GenericSuccessResponse(
        success=True,
        message="Complaint deleted successfully.",
        data=None
    )
