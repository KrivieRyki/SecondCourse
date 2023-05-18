# project/app/api/ping.py


from course_fast_api.config import get_settings, Settings
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
