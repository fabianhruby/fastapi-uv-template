"""Middleware for logging request and response details."""

import logging
import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log request and response details."""

    def __init__(self, app) -> None:
        super().__init__(app)
        self.logger = logging.getLogger(self.__class__.__name__)

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Log the request and response details."""
        start = time.perf_counter()
        try:
            response = await call_next(request)
        except Exception:
            duration_ms: float = round((time.perf_counter() - start) * 1000, 2)
            self.logger.exception(
                {
                    "method": request.method,
                    "path": request.url.path,
                    "status": None,
                    "duration_ms": duration_ms,
                },
            )
            raise

        duration_ms: float = round((time.perf_counter() - start) * 1000, 2)

        self.logger.info(
            {
                "method": request.method,
                "path": request.url.path,
                "status": response.status_code,
                "duration_ms": duration_ms,
            },
        )
        return response
