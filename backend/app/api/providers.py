from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.providers.greenhouse import GreenhouseProvider
from app.services.import_service import ImportService

router = APIRouter(prefix="/providers")


@router.get("/greenhouse/{board}")
async def greenhouse_jobs(
    board: str,
    db: Session = Depends(get_db),
):
    provider = GreenhouseProvider()

    service = ImportService()

    jobs = await service.import_jobs(
        db=db,
        provider=provider,
        board_token=board,
    )

    return jobs