# --------------------------------------------------------------------------- #
#  Router – Public endpoints (no authentication required)
# --------------------------------------------------------------------------- #

from fastapi import APIRouter, HTTPException, status

from src.db.mock_db import MEDICAL_DB
from src.schemas.public_schema import EmergencyInfo

router = APIRouter(prefix="/public", tags=["Public"])


@router.get("/emergency/{cccd}", response_model=EmergencyInfo)
async def get_emergency_info(cccd: str):
    """Return vital-signs info for emergency situations (no auth required)."""
    patient = MEDICAL_DB.get(cccd)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No medical record found for CCCD: {cccd}",
        )
    vital = patient["vital_signs"]
    return EmergencyInfo(
        blood_type=vital["blood_type"],
        allergies=vital["allergies"],
        emergency_contacts=vital["emergency_contacts"],
    )
