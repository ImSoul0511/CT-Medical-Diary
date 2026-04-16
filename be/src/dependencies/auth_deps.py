# --------------------------------------------------------------------------- #
#  FastAPI Dependencies – authentication & role guards
# --------------------------------------------------------------------------- #

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from src.core.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# ── 1. get_current_user ──────────────────────────────────────────────────── #
async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """Decode the JWT from the Authorization header and return user claims."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        username: str | None = payload.get("sub")
        role: str | None = payload.get("role")
        if username is None or role is None:
            raise credentials_exception
        return {"username": username, "role": role}
    except JWTError:
        raise credentials_exception


# ── 2. require_doctor ─────────────────────────────────────────────────────── #
async def require_doctor(current_user: dict = Depends(get_current_user)) -> dict:
    """Allow only users whose role is 'doctor'."""
    if current_user["role"] != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Doctor privileges required",
        )
    return current_user


# ── 3. require_user ──────────────────────────────────────────────────────── #
async def require_user(current_user: dict = Depends(get_current_user)) -> dict:
    """Allow only users whose role is 'user'."""
    if current_user["role"] != "user":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User privileges required",
        )
    return current_user
