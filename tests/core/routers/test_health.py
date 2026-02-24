"""Test the health check endpoint."""

from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ready"}


def test_live_check():
    """Test the live check endpoint."""
    response = client.get("/live")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "alive"}
