# --------------------------------------------------------------------------- #
#  Router – User endpoints
# --------------------------------------------------------------------------- #

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.auth_deps import require_user
from src.db.mock_db import MEDICAL_DB
from src.schemas.user_schema import PersonalInfo, PersonalInfoUpdate, DiaryEntry

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/profile", status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile_data: PersonalInfo,
    current_user: dict = Depends(require_user)
):
    """Khởi tạo và lưu thông tin profile của người dùng vào MockDB."""
    username = current_user["username"]
    
    if username not in MEDICAL_DB:
        MEDICAL_DB[username] = {
            "vital_signs": {"blood_type": "", "allergies": [], "emergency_contacts": []},
            "prescriptions": [],
            "personal_info": {},
            "habits_log": []
        }
        
    MEDICAL_DB[username]["personal_info"] = profile_data.model_dump()
    return {"message": "Profile created successfully", "data": MEDICAL_DB[username]["personal_info"]}

@router.put("/profile")
async def update_profile(
    update_data: PersonalInfoUpdate,
    current_user: dict = Depends(require_user)
):
    """Cập nhật các thông tin cá nhân của người dùng."""
    username = current_user["username"]
    
    if username not in MEDICAL_DB or not MEDICAL_DB[username].get("personal_info"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found. Please create profile first."
        )
        
    # Chỉ cập nhật các trường được truyền lên (exclude_unset=True)
    stored_data = MEDICAL_DB[username]["personal_info"]
    update_dict = update_data.model_dump(exclude_unset=True)
    
    for key, value in update_dict.items():
        stored_data[key] = value
        
    return {"message": "Profile updated successfully", "data": stored_data}

@router.post("/diary", status_code=status.HTTP_201_CREATED)
async def add_diary_entry(
    diary_data: DiaryEntry,
    current_user: dict = Depends(require_user)
):
    """Ghi nhận nhật ký thói quen, tự động gắn kèm ngày giờ."""
    username = current_user["username"]
    
    if username not in MEDICAL_DB:
        MEDICAL_DB[username] = {
            "vital_signs": {"blood_type": "", "allergies": [], "emergency_contacts": []},
            "prescriptions": [],
            "personal_info": {},
            "habits_log": []
        }
        
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_entry = f"{now_str}: {diary_data.entry}"
    
    MEDICAL_DB[username]["habits_log"].append(formatted_entry)
    
    return {"message": "Diary entry added successfully", "entry": formatted_entry}
