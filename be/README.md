# Medical Diary – Backend

Hệ thống Backend FastAPI cho dự án "Nhật ký Y tế" (Medical Diary) với cơ chế xác thực phân quyền dựa trên JWT (`user` / `doctor`).

---

## Cấu trúc thư mục dự án

```
medical_diary_backend/
├── src/
│   ├── api/
│   │   ├── auth.py            # Endpoint đăng nhập (cấp JWT token)
│   │   ├── doctor.py          # Các endpoint dành riêng cho Bác sĩ
│   │   ├── public.py          # Các endpoint công khai (không cần xác thực)
│   │   └── user.py            # Các endpoint dành riêng cho Người dùng
│   ├── core/
│   │   ├── config.py          # SECRET_KEY, ALGORITHM cho JWT
│   │   └── security.py        # Tạo/Giải mã JWT, mã hóa mật khẩu (passlib + jose)
│   ├── db/
│   │   └── mock_db.py         # Cơ sở dữ liệu giả lập (Python dicts/lists)
│   ├── dependencies/
│   │   └── auth_deps.py       # get_current_user, require_doctor, require_user
│   ├── schemas/
│   │   ├── auth_schema.py     # Token, TokenData
│   │   ├── doctor_schema.py   # Prescription, PatientMedicalInfo
│   │   ├── public_schema.py   # EmergencyInfo
│   │   └── user_schema.py     # PersonalInfo, DiaryEntry
│   └── main.py                # Khởi tạo FastAPI app, bao gồm tất cả các routers
├── requirements.txt
├── .gitignore
└── README.md                  # ← Bạn đang ở đây
```

---

## Cài đặt ban đầu (Dành cho cộng tác viên)

> **Yêu cầu:** Đảm bảo bạn đã cài đặt **Python 3.10+**.
> Kiểm tra bằng lệnh: `python --version` hoặc `py --version`

### Bước 1 – Di chuyển vào thư mục backend

```bash
cd medical_diary_backend
```

### Bước 2 – Tạo môi trường ảo (Virtual Environment)

```bash
# Windows
py -m venv venv

# macOS / Linux
python3 -m venv venv
```

### Bước 3 – Kích hoạt môi trường ảo

```bash
# Windows (PowerShell)
.\venv\Scripts\activate

# Windows (Command Prompt)
venv\Scripts\activate.bat

# macOS / Linux
source venv/bin/activate
```

Sau khi kích hoạt, bạn sẽ thấy chữ `(venv)` xuất hiện ở đầu dòng lệnh trong terminal.

### Bước 4 – Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

### Bước 5 – Chạy server phát triển (Development Server)

```bash
py -m uvicorn src.main:app --reload --port 8000
```

Server sẽ khởi chạy tại địa chỉ: **http://localhost:8000**.

---

## Tài liệu API tương tác

Sau khi server đã chạy, bạn có thể truy cập:

| Công cụ | Đường dẫn (URL) |
|---|---|
| **Swagger UI** | http://localhost:8000/docs |
| **ReDoc** | http://localhost:8000/redoc |

---

## Tài khoản giả lập (Để thử nghiệm)

| Username (CCCD) | Mật khẩu | Quyền hạn (Role) |
|---|---|---|
| `079200001234` | `user123` | user |
| `079200005678` | `user456` | user |
| `doctor01` | `doctor123` | doctor |
| `doctor02` | `doctor456` | doctor |

---

## Lưu ý quan trọng

- Dự án này sử dụng một **Cơ sở dữ liệu giả lập trong bộ nhớ** (`mock_db.py`). Mọi dữ liệu sẽ được làm mới (mất đi) khi server khởi động lại.
- Phiên bản `bcrypt==4.0.1` được cố định trong `requirements.txt` vì các phiên bản mới hơn không tương thích với backend của `passlib`.
- Luôn chạy lệnh uvicorn từ thư mục gốc `medical_diary_backend/` (đừng chạy từ thư mục `src/`) để các đường dẫn import `src.*` hoạt động chính xác.
