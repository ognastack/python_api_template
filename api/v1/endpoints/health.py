from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime

from api.deps import get_request_id
from config.settings import settings

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    environment: str
    request_id: str = None


@router.get("/", response_model=HealthResponse)
async def health_check(request_id: str = Depends(get_request_id)):
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
        request_id=request_id
    )


@router.get("/ready")
async def readiness_check():
    """Readiness check endpoint"""
    # Add checks for database, external services, etc.
    return {"status": "ready"}


@router.get("/live")
async def liveness_check():
    """Liveness check endpoint"""
    return {"status": "alive"}