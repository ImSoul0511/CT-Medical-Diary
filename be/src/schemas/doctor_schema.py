# --------------------------------------------------------------------------- #
#  Pydantic schemas – Doctor endpoints
# --------------------------------------------------------------------------- #

from pydantic import BaseModel


class PrescriptionItem(BaseModel):
    """A single prescription entry."""
    disease: str
    medicines: list[str]


class AddPrescriptionRequest(BaseModel):
    """Body for POST /doctor/prescription."""
    cccd: str
    prescription: PrescriptionItem


class PatientMedicalInfo(BaseModel):
    """Response for GET /doctor/patient/{cccd}."""
    vital_signs: dict
    prescriptions: list[dict]
