# --------------------------------------------------------------------------- #
#  Pydantic schemas – Doctor endpoints
# --------------------------------------------------------------------------- #

from pydantic import BaseModel, Field


# ── Shared building blocks ─────────────────────────────────────────────────── #

class PrescriptionItem(BaseModel):
    """A single prescription entry (used in responses)."""
    disease: str
    medicines: list[str]


# ── GET /doctor/patient-info/{cccd} ──────────────────────────────────────── #

class PatientMedicalInfo(BaseModel):
    """Response body for the patient-info endpoint."""
    vital_signs: dict
    prescriptions: list[dict]


# ── POST /doctor/prescribe ────────────────────────────────────────────────── #

class MedicationEntry(BaseModel):
    """
    A single medication with its details stored as a flexible JSON object.
    Doctors can add any key-value pairs (name, dose, frequency, duration, …).
    """
    name: str = Field(..., description="Medication name, e.g. 'Amoxicillin 500mg'")
    dose: str | None = Field(None, description="Dosage, e.g. '1 tablet'")
    frequency: str | None = Field(None, description="How often, e.g. '3 times/day'")
    duration: str | None = Field(None, description="Duration, e.g. '7 days'")
    notes: str | None = Field(None, description="Additional notes")


class PrescribeRequest(BaseModel):
    """Body for POST /doctor/prescribe."""
    cccd: str = Field(..., description="National ID of the patient")
    disease: str = Field(..., description="Diagnosed disease / condition")
    medications: list[MedicationEntry] = Field(
        ..., description="List of medication objects (stored as dict/JSON in DB)"
    )


class PrescribeResponse(BaseModel):
    """Response returned after a successful prescription write."""
    message: str
    cccd: str
    prescription_index: int = Field(..., description="Zero-based index of the new record")


# ── Legacy alias (kept for backward-compatibility) ─────────────────────────── #
class AddPrescriptionRequest(BaseModel):
    """Legacy body for POST /doctor/prescription (simple form)."""
    cccd: str
    prescription: PrescriptionItem
