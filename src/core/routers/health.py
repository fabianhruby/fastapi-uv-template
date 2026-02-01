"""Core router with health and live checks included."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

core_router = APIRouter()


@core_router.get(path="/health")
async def health() -> JSONResponse:
    """Check if the app is healthy.

    Return
    -------
    JSONResponse
        A JSON response indicating the health status of the app.
    """
    return {"status": "ready"}  # ty:ignore[invalid-return-type]


@core_router.get(path="/live")
async def live() -> JSONResponse:
    """Check if the app is live.

    Returns
    -------
    JSONResponse
        A JSON response indicating the live status of the app.
    """
    return {"status": "alive"}  # ty:ignore[invalid-return-type]
