# --------------------------------------------------------------------------- #
#  Router – Doctor endpoints
# --------------------------------------------------------------------------- #

from fastapi import APIRouter

router = APIRouter(prefix="/doctor", tags=["Doctor"])

# TODO: Implement GET /doctor/patient/{cccd}
# - Requires: Depends(require_doctor)
# - Returns "vital_signs" and "prescriptions" from MEDICAL_DB

# TODO: Implement POST /doctor/prescription
# - Requires: Depends(require_doctor)
# - Accepts CCCD + prescription schema (disease name + list of medicines)
# - Appends to patient's "prescriptions" list in MEDICAL_DB
