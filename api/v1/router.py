from fastapi import APIRouter

from api.v1.endpoints import health, check

api_router = APIRouter()

api_router.include_router(
    health.router,
    prefix="/health",
    tags=["health"]
)


api_router.include_router(
    check.router,
    prefix="/check",
    tags=["check"]
)