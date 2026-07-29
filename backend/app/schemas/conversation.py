from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from uuid import UUID

from app.schemas.common import MessageSender

class ConversationMessageBase(BaseModel):
    """Base schema for chat conversation messages"""
    sender: MessageSender
    message: str = Field(..., min_length=1)

class ConversationMessageCreate(ConversationMessageBase):
    """Schema for adding a new conversation message"""
    pass

class ConversationMessageResponse(ConversationMessageBase):
    """Schema for returning conversation messages"""
    message_id: UUID
    complaint_id: UUID
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
