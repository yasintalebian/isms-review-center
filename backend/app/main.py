from fastapi import FastAPI

from backend.app.config import get_settings

settings = get_settings()

app = FastAPI(
    title="ISMS Review Center API",
    description="Review dashboard API and test-server integration boundary.",
    version="0.1.0",
)


@app.get("/health", tags=["operations"])
async def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.app_env}


@app.get("/api/v1", tags=["operations"])
async def api_root() -> dict[str, str]:
    return {
        "name": "ISMS Review Center API",
        "version": "0.1.0",
        "status": "scaffold",
    }
