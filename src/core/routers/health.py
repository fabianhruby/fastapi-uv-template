"""Core router with health and live checks included."""

from fastapi import APIRouter

core_router = APIRouter()


@core_router.get(path="/health")
async def health() -> dict[str, str]:
    """Check if the app is healthy.

    Return
    -------
    dict
        A JSON response indicating the health status of the app.
    """
    return {"status": "ready"}


@core_router.get(path="/live")
async def live() -> dict[str, str]:
    """Check if the app is live.

    Returns
    -------
    dict
        A JSON response indicating the live status of the app.
    """
    return {"status": "alive"}
