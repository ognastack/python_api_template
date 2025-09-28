from fastapi import APIRouter, Depends, Header
from pydantic import BaseModel, Field
from datetime import datetime
from api.deps import get_request_id,get_current_user
from config.settings import settings
from typing import Optional

router = APIRouter()


class CheckResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    environment: str
    request_id: str = None
    user_id: Optional[str] = Field(..., description="User biography")


@router.get("/", response_model=CheckResponse)
async def check_root(request_id: str = Depends(get_request_id), user_id: str = Depends(get_current_user)):
    """Health check endpoint"""
    return CheckResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
        request_id=request_id,
        user_id=user_id
    )
