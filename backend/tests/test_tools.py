"""
Tool layer unit tests.
Tests BaseTool contract enforcement and individual tool subclasses
with mocked LLM calls.
"""
import pytest
from unittest.mock import AsyncMock, patch, MagicMock

from app.tools.base_tool import BaseTool


class DummyTool(BaseTool):
    """Concrete tool subclass for testing the base contract."""

    @property
    def tool_name(self) -> str:
        return "DummyTool"

    @property
    def description(self) -> str:
        return "A tool used only for testing."

    async def _execute(self, **kwargs):
        return {"result": "ok"}


class FailingTool(BaseTool):
    """Tool that always raises an exception during execution."""

    @property
    def tool_name(self) -> str:
        return "FailingTool"

    @property
    def description(self) -> str:
        return "Tool that fails."

    async def _execute(self, **kwargs):
        raise RuntimeError("Simulated failure")


class InvalidInputTool(BaseTool):
    """Tool that fails input validation."""

    @property
    def tool_name(self) -> str:
        return "InvalidInputTool"

    @property
    def description(self) -> str:
        return "Tool with strict input validation."

    def validate_input(self, **kwargs) -> bool:
        return False

    async def _execute(self, **kwargs):
        return {}


@pytest.mark.asyncio
class TestBaseTool:
    """Tests for the BaseTool abstract base class contract."""

    async def test_successful_execution(self):
        """Tool should return result on successful execution."""
        tool = DummyTool()
        result = await tool.execute()
        assert result == {"result": "ok"}

    async def test_error_returns_structured_dict(self):
        """Failing tool should return error dict, not crash."""
        tool = FailingTool()
        result = await tool.execute()
        assert result["error"] is True
        assert "Simulated failure" in result["message"]
        assert result["source"] == "FailingTool"

    async def test_input_validation_failure(self):
        """Tool with invalid input should return error dict."""
        tool = InvalidInputTool()
        result = await tool.execute()
        assert result["error"] is True
        assert "validation failed" in result["message"].lower()

    async def test_tool_name_property(self):
        """Tool name property should return the correct name."""
        tool = DummyTool()
        assert tool.tool_name == "DummyTool"

    async def test_tool_description_property(self):
        """Tool description property should return the correct value."""
        tool = DummyTool()
        assert tool.description == "A tool used only for testing."
