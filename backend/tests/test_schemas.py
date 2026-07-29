"""
Unit tests for Pydantic v2 schemas.
Validates field constraints, required fields, optional fields,
email validation, regex patterns, and enum enforcement.
"""
import pytest
from datetime import date, datetime
from uuid import uuid4

from app.schemas.complaint import (
    ComplaintCreate,
    ComplaintUpdate,
    ComplaintDetailsCreate,
)
from app.schemas.customer import CustomerCreate
from app.schemas.common import (
    ComplaintStatus,
    RiskLevel,
    GenericSuccessResponse,
    ValidationResponse,
)


class TestComplaintSchemas:
    """Tests for ComplaintCreate, ComplaintUpdate, and ComplaintDetails."""

    def test_complaint_create_valid(self):
        """A minimal valid complaint only needs a description."""
        c = ComplaintCreate(complaint_description="Broken tablets in shipment")
        assert c.complaint_description == "Broken tablets in shipment"
        assert c.customer is None
        assert c.product is None

    def test_complaint_create_empty_description_rejected(self):
        """Description cannot be empty string."""
        with pytest.raises(Exception):
            ComplaintCreate(complaint_description="")

    def test_complaint_create_missing_description_rejected(self):
        """Description is required."""
        with pytest.raises(Exception):
            ComplaintCreate()

    def test_complaint_create_with_nested_customer(self):
        """Complaint can include inline customer data."""
        c = ComplaintCreate(
            complaint_description="Issue reported",
            customer=CustomerCreate(customer_name="John Doe", email="john@example.com"),
        )
        assert c.customer.customer_name == "John Doe"

    def test_complaint_update_partial(self):
        """Update schema allows partial fields."""
        u = ComplaintUpdate(complaint_category="Packaging")
        assert u.complaint_category == "Packaging"
        assert u.complaint_description is None

    def test_complaint_update_status_enum(self):
        """Update schema enforces ComplaintStatus enum."""
        u = ComplaintUpdate(complaint_status=ComplaintStatus.IN_PROGRESS)
        assert u.complaint_status == ComplaintStatus.IN_PROGRESS

    def test_complaint_details_quantity_non_negative(self):
        """Quantity affected must be >= 0."""
        with pytest.raises(Exception):
            ComplaintDetailsCreate(quantity_affected=-5)

    def test_complaint_details_valid(self):
        """Valid details with all fields."""
        d = ComplaintDetailsCreate(
            defect_type="Discoloration",
            quantity_affected=100,
            location="Warehouse A",
        )
        assert d.defect_type == "Discoloration"
        assert d.quantity_affected == 100


class TestCustomerSchemas:
    """Tests for customer validation including email and phone regex."""

    def test_customer_valid_email(self):
        """Valid email should pass."""
        c = CustomerCreate(customer_name="Jane", email="jane@pharma.com")
        assert c.email == "jane@pharma.com"

    def test_customer_invalid_email_rejected(self):
        """Invalid email format should be rejected."""
        with pytest.raises(Exception):
            CustomerCreate(email="not-an-email")

    def test_customer_valid_phone(self):
        """Valid phone patterns should pass."""
        c = CustomerCreate(phone="+1 555-123-4567")
        assert c.phone == "+1 555-123-4567"

    def test_customer_invalid_phone_rejected(self):
        """Invalid phone should be rejected by regex."""
        with pytest.raises(Exception):
            CustomerCreate(phone="abc")


class TestCommonSchemas:
    """Tests for shared enums and response wrappers."""

    def test_complaint_status_values(self):
        """Verify all expected status values exist."""
        assert ComplaintStatus.DRAFT == "Draft"
        assert ComplaintStatus.RESOLVED == "Resolved"

    def test_risk_level_values(self):
        """Verify all risk levels."""
        assert RiskLevel.LOW == "Low"
        assert RiskLevel.CRITICAL == "Critical"

    def test_generic_success_response(self):
        """Success wrapper defaults."""
        r = GenericSuccessResponse(data={"key": "val"})
        assert r.success is True
        assert r.data == {"key": "val"}

    def test_validation_response(self):
        """ValidationResponse enforces score bounds."""
        v = ValidationResponse(is_valid=True, completeness_score=85)
        assert v.completeness_score == 85

    def test_validation_response_score_out_of_range(self):
        """Score > 100 should fail."""
        with pytest.raises(Exception):
            ValidationResponse(is_valid=True, completeness_score=150)
