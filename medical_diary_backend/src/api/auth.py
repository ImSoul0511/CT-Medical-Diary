# --------------------------------------------------------------------------- #
#  Router – Authentication (login)
# --------------------------------------------------------------------------- #

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.core.security import verify_password, create_access_token
from src.db.mock_db import USERS_DB
from src.schemas.auth_schema import Token

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ── Helper ────────────────────────────────────────────────────────────────── #
def _find_user(identifier: str) -> dict | None:
    """
    Look up a user by username OR CCCD.
    In USERS_DB the username field doubles as the CCCD for regular users,
    so a single equality check covers both cases.
    """
    for user in USERS_DB:
        if user["username"] == identifier:
            return user
    return None


# ── POST /auth/login ──────────────────────────────────────────────────────── #
@router.post("/login", response_model=Token, summary="Login and obtain a JWT")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate with **username or CCCD** + **password**.

    - Returns a Bearer JWT containing `sub` (username/CCCD) and `role` claims.
    - Raises **401** if the credentials are invalid.
    """
    user = _find_user(form_data.username)

    if user is None or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username/CCCD or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": user["username"], "role": user["role"]}
    )
    return Token(access_token=access_token, token_type="bearer")
