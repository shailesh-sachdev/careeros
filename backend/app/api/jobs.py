from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.services.job_query_service import JobQueryService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get("")
async def list_jobs(
    db: Session = Depends(get_db),
):

    service = JobQueryService()

    jobs = service.list_jobs(db)

    return jobs