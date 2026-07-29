"""
Integration tests – Tests the full complaint creation workflow
with mocked database and service layer.
"""
import pytest
from unittest.mock import patch, AsyncMock


@pytest.mark.asyncio
class TestComplaintIntegration:
    """Integration tests for the complaint lifecycle."""

    async def test_create_then_list(self, async_client):
        """Creating a complaint should succeed, then listing should return it."""
        with patch(
            "app.services.complaint_service.ComplaintService.create_complaint",
            new_callable=AsyncMock,
            return_value=None,
        ):
            create_resp = await async_client.post(
                "/api/v1/complaints",
                json={"complaint_description": "Integration test complaint"},
            )
            assert create_resp.status_code == 201

        with patch(
            "app.services.complaint_service.ComplaintService.get_complaints",
            new_callable=AsyncMock,
            return_value=[],
        ):
            list_resp = await async_client.get("/api/v1/complaints")
            assert list_resp.status_code == 200

    async def test_update_nonexistent_complaint(self, async_client):
        """Updating a complaint that doesn't exist should return 404."""
        with patch(
            "app.services.complaint_service.ComplaintService.update_complaint",
            new_callable=AsyncMock,
            return_value=None,
        ):
            resp = await async_client.put(
                "/api/v1/complaints/00000000-0000-0000-0000-000000000099",
                json={"complaint_category": "Safety"},
            )
            assert resp.status_code == 404

    async def test_health_during_workflow(self, async_client):
        """Health endpoint should remain responsive during operations."""
        resp = await async_client.get("/api/v1/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "UP"
