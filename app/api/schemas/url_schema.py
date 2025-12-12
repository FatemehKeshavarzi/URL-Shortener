from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from typing import Optional, Literal


class URLCreate(BaseModel):
    original_url: HttpUrl = Field(max_length=255)


class URLResponse(BaseModel):
    id:  Optional[int] = None
    original_url: Optional[str] = None
    short_code: Optional[str] = None
    created_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    message: Optional[str] = None
    status: Literal["success", "failure"]

    class Config:
        from_attributes = True


