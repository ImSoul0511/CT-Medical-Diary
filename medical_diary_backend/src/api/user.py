# --------------------------------------------------------------------------- #
#  Router – User endpoints
# --------------------------------------------------------------------------- #

from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["User"])

# TODO: Implement POST /user/profile
# - Requires: Depends(require_user)
# - Submits initial "personal_info" to MEDICAL_DB

# TODO: Implement PUT /user/profile
# - Requires: Depends(require_user)
# - Updates existing "personal_info" in MEDICAL_DB

# TODO: Implement POST /user/diary
# - Requires: Depends(require_user)
# - Accepts a string entry, appends it to "habits_log" list in MEDICAL_DB
