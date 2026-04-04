# --------------------------------------------------------------------------- #
#  Pydantic schemas – Authentication
# --------------------------------------------------------------------------- #

from pydantic import BaseModel


class Token(BaseModel):
    """Schema returned after successful login."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Decoded JWT payload."""
    sub: str          # username / CCCD
    role: str         # "user" | "doctor"
