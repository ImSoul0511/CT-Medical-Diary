# --------------------------------------------------------------------------- #
#  Medical Diary – FastAPI Application Entry Point
# --------------------------------------------------------------------------- #

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import auth, doctor, public, user

app = FastAPI(
    title="Medical Diary API",
    description="A role-based medical diary system with JWT authentication.",
    version="1.0.0",
)

# ── CORS (allow all origins for development) ─────────────────────────────── #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Register Routers ─────────────────────────────────────────────────────── #
app.include_router(auth.router)
app.include_router(doctor.router)
app.include_router(public.router)
app.include_router(user.router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Medical Diary API"}
