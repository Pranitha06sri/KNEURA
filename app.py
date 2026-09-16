from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent
FRONTEND = ROOT / "frontend"

app = FastAPI(
    title="KNEURA",
    version="3.3"
)

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "KNEURA",
        "platform": "Vercel"
    }

# Keep this AFTER the API routes.
# It serves frontend/index.html at /
app.mount(
    "/",
    StaticFiles(directory=str(FRONTEND), html=True),
    name="frontend"
)
