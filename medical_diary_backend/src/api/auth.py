# --------------------------------------------------------------------------- #
#  Router – Authentication (login)
# --------------------------------------------------------------------------- #

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.db.mock_db import USERS_DB
from src.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Xác thực tài khoản, trả về JWT Token."""
    user_dict = next((u for u in USERS_DB if u["username"] == form_data.username), None)
    
    if not user_dict or not verify_password(form_data.password, user_dict["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sai thông tin đăng nhập",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token = create_access_token(
        data={"sub": user_dict["username"], "role": user_dict["role"]}
    )
    return {"access_token": access_token, "token_type": "bearer"}
