from fastapi import FastAPI

from app.api.providers import router as provider_router
from app.api.jobs import router as jobs_router
from app.api.applications import router as applications_router


app = FastAPI(
    title="CareerOS API",
    version="1.0.0",
)

app.include_router(provider_router)
app.include_router(jobs_router)
app.include_router(applications_router)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "application": app.title,
        "version": app.version,
    }