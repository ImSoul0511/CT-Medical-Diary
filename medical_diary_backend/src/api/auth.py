# --------------------------------------------------------------------------- #
#  Router – Authentication (login)
# --------------------------------------------------------------------------- #

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])

# TODO: Implement POST /login endpoint
# - Accept OAuth2PasswordRequestForm (username/CCCD + password)
# - Verify credentials against USERS_DB
# - Return JWT token with "sub" and "role" claims
