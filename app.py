from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="KNEURA",
    version="3.3"
)

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "KNEURA"
    }

@app.get("/", include_in_schema=False)
def homepage():
    return RedirectResponse(url="/index.html")
