from pydantic import BaseModel, HttpUrl, Field, validator
from datetime import datetime
from typing import Optional, Literal


class URLCreate(BaseModel):
    original_url: HttpUrl

    @validator("original_url", pre=True)
    def validate_url(cls, v):
        if isinstance(v, str):
            v = v.strip()
        return v


class URLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    created_at: datetime
    expires_at: datetime | None = None



class URLListSchema(BaseModel):
    id: int
    original_url: str
    short_code: str
    created_at: datetime
    expires_at: datetime | None = None