from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, constr
from uuid import UUID

class CustomerBase(BaseModel):
    """Base schema for customer properties"""
    customer_name: Optional[str] = Field(None, max_length=255)
    customer_type: Optional[str] = Field(None, max_length=100)
    country: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = Field(None, description="Valid email address")
    # Basic regex for phone numbers (allows +, digits, spaces, hyphens)
    phone: Optional[str] = Field(None, pattern=r"^\+?[0-9\s\-()]{7,20}$")

class CustomerCreate(CustomerBase):
    """Schema for creating a new customer"""
    pass

class CustomerUpdate(CustomerBase):
    """Schema for updating an existing customer"""
    pass

class CustomerResponse(CustomerBase):
    """Schema for returning customer information"""
    customer_id: UUID

    model_config = ConfigDict(from_attributes=True)
