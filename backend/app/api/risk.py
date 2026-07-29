from fastapi import APIRouter, Depends, status
from uuid import UUID

from app.schemas.common import GenericSuccessResponse
from app.schemas.risk import RiskAssessmentResponse
from app.services.risk_service import RiskService
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("", response_model=GenericSuccessResponse[dict], status_code=status.HTTP_200_OK)
async def generate_risk(
    complaint_id: UUID,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Generate or regenerate AI-assisted risk analysis based on the latest validated complaint information.
    """
    # Delegate to service
    result = await RiskService.generate_assessment(db, complaint_id)
    
    return GenericSuccessResponse(
        success=True,
        message="Risk assessment generated successfully.",
        data=result
    )
