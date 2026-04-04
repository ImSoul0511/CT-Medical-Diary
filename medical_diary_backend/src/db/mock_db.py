# --------------------------------------------------------------------------- #
#  Mock database – in-memory Python structures
# --------------------------------------------------------------------------- #

from src.core.security import hash_password

# ══════════════════════════════════════════════════════════════════════════════
#  USERS_DB  –  list of registered users
#  Fields: username (== CCCD), hashed_password, role ("user" | "doctor")
# ══════════════════════════════════════════════════════════════════════════════
USERS_DB: list[dict] = [
    {
        "username": "079200001234",          # CCCD of a regular user
        "hashed_password": hash_password("user123"),
        "role": "user",
    },
    {
        "username": "079200005678",          # CCCD of another user
        "hashed_password": hash_password("user456"),
        "role": "user",
    },
    {
        "username": "doctor01",              # doctor account
        "hashed_password": hash_password("doctor123"),
        "role": "doctor",
    },
    {
        "username": "doctor02",
        "hashed_password": hash_password("doctor456"),
        "role": "doctor",
    },
]

# ══════════════════════════════════════════════════════════════════════════════
#  MEDICAL_DB  –  keyed by CCCD
#  Each entry stores: vital_signs, prescriptions, personal_info, habits_log
# ══════════════════════════════════════════════════════════════════════════════
MEDICAL_DB: dict[str, dict] = {
    "079200001234": {
        "vital_signs": {
            "blood_type": "O+",
            "allergies": ["Penicillin", "Pollen"],
            "emergency_contacts": [
                {"name": "Nguyen Van A", "phone": "0901234567", "relation": "Father"},
            ],
        },
        "prescriptions": [
            {
                "disease": "Flu",
                "medicines": ["Paracetamol 500mg", "Vitamin C 1000mg"],
            },
        ],
        "personal_info": {
            "full_name": "Tran Thi B",
            "date_of_birth": "2000-05-15",
            "gender": "Female",
            "phone": "0912345678",
            "address": "123 Le Loi, HCMC",
        },
        "habits_log": [
            "2026-04-01: Mild headache after staying up late.",
            "2026-04-02: Felt dizzy in the morning, skipped breakfast.",
        ],
    },
    "079200005678": {
        "vital_signs": {
            "blood_type": "A+",
            "allergies": [],
            "emergency_contacts": [
                {"name": "Le Van C", "phone": "0909876543", "relation": "Mother"},
            ],
        },
        "prescriptions": [],
        "personal_info": {
            "full_name": "Pham Van D",
            "date_of_birth": "1998-11-20",
            "gender": "Male",
            "phone": "0987654321",
            "address": "456 Nguyen Hue, HCMC",
        },
        "habits_log": [
            "2026-04-03: Regular exercise, feeling good.",
        ],
    },
}
