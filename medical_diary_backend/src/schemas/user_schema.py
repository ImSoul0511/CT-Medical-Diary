# --------------------------------------------------------------------------- #
#  Pydantic schemas – User endpoints
# --------------------------------------------------------------------------- #

from typing import Optional
from pydantic import BaseModel


class PersonalInfo(BaseModel):
    """Schema for creating / updating user profile."""
    full_name: str
    date_of_birth: str
    gender: str
    phone: str
    address: str


class PersonalInfoUpdate(BaseModel):
    """Schema for partial profile update (all fields optional)."""
    full_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class DiaryEntry(BaseModel):
    """Body for POST /user/diary."""
    entry: str
