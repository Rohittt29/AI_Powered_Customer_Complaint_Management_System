"""
Service layer unit tests.
Tests the ComplaintService static methods with mocked database sessions.
"""
import pytest
from unittest.mock import MagicMock, AsyncMock
from uuid import uuid4

from app.services.complaint_service import ComplaintService
from app.schemas.complaint import ComplaintCreate, ComplaintUpdate


@pytest.mark.asyncio
class TestComplaintService:
    """Unit tests for ComplaintService methods."""

    async def test_get_complaints_returns_list(self, mock_db):
        """get_complaints should return a list (empty by default for stub)."""
        result = await ComplaintService.get_complaints(mock_db)
        assert isinstance(result, list)

    async def test_delete_complaint_returns_true(self, mock_db):
        """delete_complaint stub returns True."""
        result = await ComplaintService.delete_complaint(mock_db, uuid4())
        assert result is True

    async def test_create_complaint_accepts_valid_schema(self, mock_db):
        """create_complaint should accept a valid ComplaintCreate."""
        schema = ComplaintCreate(complaint_description="Test complaint")
        # The stub currently returns None; we just verify no exception
        result = await ComplaintService.create_complaint(mock_db, schema)
        assert result is None  # Stub behavior

    async def test_get_complaint_returns_none_for_unknown_id(self, mock_db):
        """get_complaint stub returns None."""
        result = await ComplaintService.get_complaint(mock_db, uuid4())
        assert result is None
