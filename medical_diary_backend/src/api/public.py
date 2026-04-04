# --------------------------------------------------------------------------- #
#  Router – Public endpoints (no authentication required)
# --------------------------------------------------------------------------- #

from fastapi import APIRouter

router = APIRouter(prefix="/public", tags=["Public"])

# TODO: Implement GET /public/emergency/{cccd}
# - No authentication required
# - Returns ONLY "vital_signs" (blood type, allergies, emergency contacts)
#   from MEDICAL_DB for the given CCCD
