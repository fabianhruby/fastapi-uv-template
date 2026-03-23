from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.config import settings
from core.app import create_app


@pytest.fixture
def client():
    mock_redis = AsyncMock()
    mock_redis.eval.return_value = 1

    with patch("core.app.get_redis_client", return_value=mock_redis):
        app = create_app(settings=settings)
        with TestClient(app) as client:
            yield client
