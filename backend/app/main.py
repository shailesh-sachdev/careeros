from fastapi import FastAPI

from app.api.providers import router as provider_router

app = FastAPI(
    title="CareerOS API",
    version="1.0.0",
)

app.include_router(provider_router)


@app.get("/")
async def root():
    return {
        "status": "ok",
        "application": app.title,
        "version": app.version,
    }