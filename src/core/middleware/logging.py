"""Logging Middleware to log request and response details."""

import logging
import time

from logging import Logger

from fastapi import Request, Response
from starlette.applications import Starlette
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log request and response details."""

    def __init__(self, app: Starlette):
        super().__init__(app)
        self.logger: Logger = logging.getLogger(name=self.__class__.__name__)

    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        """Dispatch method to handle the request and log details.

        Parameters
        ----------
        request : Request
            The incoming request object.
        call_next : callable
            The next middleware or route handler to be called.

        Returns
        -------
        Response
            The outgoing response object.
        """
        start_time: int | float = time.perf_counter()
        response: Response = await call_next(request)
        end_time: int | float = time.perf_counter()

        duration_ms: int = round(number=(end_time - start_time) * 1000, ndigits=2)

        log_message: dict[str, str] = {
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration_ms": duration_ms,
        }

        self.logger.info(msg=log_message)

        return response
