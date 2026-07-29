"""
API route tests – Uses httpx AsyncClient to test all REST endpoints.
All database and service layer calls are mocked.
"""
import pytest
from unittest.mock import patch, AsyncMock


@pytest.mark.asyncio
class TestHealthEndpoint:
    """Tests for the /api/v1/health endpoint."""

    async def test_health_returns_200(self, async_client):
        """Health check should return status UP."""
        response = await async_client.get("/api/v1/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "UP"
        assert "version" in data


@pytest.mark.asyncio
class TestComplaintEndpoints:
    """Tests for /api/v1/complaints CRUD endpoints."""

    async def test_list_complaints_returns_200(self, async_client):
        """GET /complaints should return a success envelope."""
        with patch(
            "app.services.complaint_service.ComplaintService.get_complaints",
            new_callable=AsyncMock,
            return_value=[],
        ):
            response = await async_client.get("/api/v1/complaints")
            assert response.status_code == 200
            body = response.json()
            assert body["success"] is True

    async def test_create_complaint_returns_201(self, async_client):
        """POST /complaints should accept valid data."""
        with patch(
            "app.services.complaint_service.ComplaintService.create_complaint",
            new_callable=AsyncMock,
            return_value=None,
        ):
            response = await async_client.post(
                "/api/v1/complaints",
                json={"complaint_description": "Tablets crumbled during transit"},
            )
            assert response.status_code == 201

    async def test_create_complaint_validation_error(self, async_client):
        """POST /complaints with empty body should return 422."""
        response = await async_client.post("/api/v1/complaints", json={})
        assert response.status_code == 422

    async def test_get_complaint_not_found(self, async_client):
        """GET /complaints/{id} with unknown ID should return 404."""
        with patch(
            "app.services.complaint_service.ComplaintService.get_complaint",
            new_callable=AsyncMock,
            return_value=None,
        ):
            response = await async_client.get(
                "/api/v1/complaints/00000000-0000-0000-0000-000000000001"
            )
            assert response.status_code == 404

    async def test_delete_complaint_returns_200(self, async_client):
        """DELETE /complaints/{id} with valid ID."""
        with patch(
            "app.services.complaint_service.ComplaintService.delete_complaint",
            new_callable=AsyncMock,
            return_value=True,
        ):
            response = await async_client.delete(
                "/api/v1/complaints/00000000-0000-0000-0000-000000000001"
            )
            assert response.status_code == 200
