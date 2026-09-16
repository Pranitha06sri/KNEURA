import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend 1"

sys.path.insert(0, str(BACKEND))

from fastapi import FastAPI
from app.main import app as kneura_backend

app = FastAPI()

app.mount("/api", kneura_backend)

@app.get("/api/health-vercel")
def health_vercel():
    return {
        "status": "ok",
        "service": "KNEURA",
        "platform": "Vercel"
    }
