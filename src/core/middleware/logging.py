"""Logging Middleware to log request and response details."""

import logging
import time

from logging import Logger

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log request and response details."""

    def __init__(self, app: FastAPI):
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

        log_message: dict[str, str] = {
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "elapsed_seconds": f"{(end_time - start_time)}",
        }

        self.logger.info(msg=log_message)

        return response
