from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from uuid import UUID

class ProductBase(BaseModel):
    """Base schema for product properties"""
    product_name: Optional[str] = Field(None, max_length=255)
    product_code: Optional[str] = Field(None, max_length=100)
    batch_number: Optional[str] = Field(None, max_length=100)
    manufacturing_date: Optional[date] = None
    expiry_date: Optional[date] = None

class ProductCreate(ProductBase):
    """Schema for creating a new product"""
    pass

class ProductUpdate(ProductBase):
    """Schema for updating an existing product"""
    pass

class ProductResponse(ProductBase):
    """Schema for returning product information"""
    product_id: UUID

    model_config = ConfigDict(from_attributes=True)
