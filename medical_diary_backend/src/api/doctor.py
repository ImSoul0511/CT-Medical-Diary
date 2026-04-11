# --------------------------------------------------------------------------- #
#  Router – Doctor endpoints  (role-protected)
# --------------------------------------------------------------------------- #

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status

from src.db.mock_db import MEDICAL_DB
from src.dependencies.auth_deps import require_doctor
from src.schemas.doctor_schema import (
    PatientMedicalInfo,
    PrescribeRequest,
    PrescribeResponse,
)

router = APIRouter(prefix="/doctor", tags=["Doctor"])


# ── GET /doctor/patient-info/{cccd} ──────────────────────────────────────── #
@router.get(
    "/patient-info/{cccd}",
    response_model=PatientMedicalInfo,
    summary="Retrieve a patient's vital signs and prescription history",
)
async def get_patient_info(
    cccd: str,
    current_doctor: dict = Depends(require_doctor),
):
    """
    **Doctor only.**  
    Returns the patient's:
    - `vital_signs` – blood type, allergies, emergency contacts (Tầng sinh tử)
    - `prescriptions` – full prescription history

    - **403** if the caller is not a doctor.  
    - **404** if no patient with the given CCCD exists.
    """
    patient = MEDICAL_DB.get(cccd)
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with CCCD '{cccd}' not found",
        )

    return PatientMedicalInfo(
        vital_signs=patient["vital_signs"],
        prescriptions=patient["prescriptions"]
    )


# ── POST /doctor/prescribe ────────────────────────────────────────────────── #
@router.post(
    "/prescribe",
    response_model=PrescribeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new prescription for a patient",
)
async def prescribe(
    body: PrescribeRequest,
    current_doctor: dict = Depends(require_doctor),
):
    """
    **Doctor only.**  
    Creates a new prescription record in the patient's medical file.

    The `medications` field is a **list of JSON objects** (each object may carry
    `name`, `dose`, `frequency`, `duration`, and free-form `notes`), stored
    directly as a dict in the MockDB so the schema remains flexible.

    - **403** if the caller is not a doctor.  
    - **404** if no patient with the given CCCD exists.
    """
    patient = MEDICAL_DB.get(body.cccd)
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with CCCD '{body.cccd}' not found",
        )

    # Build the prescription record; medications stored as list[dict]
    new_prescription: dict = {
        "disease": body.disease,
        "medications": [med.model_dump(exclude_none=True) for med in body.medications],
        "prescribed_by": current_doctor["username"],
        "prescribed_at": datetime.now(timezone.utc).isoformat(),
    }

    patient["prescriptions"].append(new_prescription)
    prescription_index = len(patient["prescriptions"]) - 1

    return PrescribeResponse(
        message="Prescription added successfully",
        cccd=body.cccd,
        prescription_index=prescription_index,
    )
