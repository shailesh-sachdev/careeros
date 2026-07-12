from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.manager import AIManager

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


class PromptRequest(BaseModel):
    system_prompt: str
    user_prompt: str


@router.post("/generate")
async def generate(
    request: PromptRequest,
):

    manager = AIManager()

    response = await manager.generate(
        request.system_prompt,
        request.user_prompt,
    )

    return {
        "response": response,
    }