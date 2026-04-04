# --------------------------------------------------------------------------- #
#  Pydantic schemas – Public endpoints
# --------------------------------------------------------------------------- #

from pydantic import BaseModel


class EmergencyInfo(BaseModel):
    """Response for GET /public/emergency/{cccd}."""
    blood_type: str
    allergies: list[str]
    emergency_contacts: list[dict]
