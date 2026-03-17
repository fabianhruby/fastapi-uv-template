"""Test the health check endpoint."""

from fastapi import status


def test_health_check(client):
    """Test the /health endpoint returns 200 with ready status."""
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ready"}


def test_live_check(client):
    """Test the /live endpoint returns 200 with alive status."""
    response = client.get("/live")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "alive"}
