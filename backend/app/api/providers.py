from fastapi import APIRouter

from app.providers.greenhouse import GreenhouseProvider
from app.services.import_service import ImportService

router = APIRouter(prefix="/providers")


@router.get("/greenhouse/{board}")
async def greenhouse_jobs(board: str):
    provider = GreenhouseProvider()
    service = ImportService()

    jobs = await service.import_jobs(
        provider,
        board_token=board,
    )

    return jobs