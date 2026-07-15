from fastapi import FastAPI

from app.api.providers import router as provider_router
from app.api.jobs import router as jobs_router
from app.api.applications import router as applications_router
from app.api.saved_jobs import router as saved_jobs_router
from app.api.candidate_profile import router as candidate_profile_router
from app.api.ai import router as ai_router
from app.api.resume import router as resume_router
from app.api.resume_ai import router as resume_ai_router
from app.api.job_match import router as job_match_router
from app.api.resume_tailor import router as resume_tailor_router









app = FastAPI(
    title="CareerOS API",
    version="1.0.0",
)

app.include_router(provider_router)
app.include_router(jobs_router)
app.include_router(applications_router)
app.include_router(saved_jobs_router)
app.include_router(candidate_profile_router)
app.include_router(ai_router)
app.include_router(resume_router)
app.include_router(resume_ai_router)
app.include_router(job_match_router)
app.include_router(resume_tailor_router)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "application": app.title,
        "version": app.version,
    }