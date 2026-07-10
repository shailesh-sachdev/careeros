from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title="CareerOS API",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "status": "ok",
        "application": app.title,
        "version": app.version,
        "database": settings.DATABASE_URL.split("@")[-1],
    }