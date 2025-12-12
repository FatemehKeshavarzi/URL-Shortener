from pydantic import BaseModel, HttpUrl, validator, Field, AnyHttpUrl
from datetime import datetime
from typing import Optional, Literal

class URLCreate(BaseModel):
    original_url: HttpUrl 

    @validator("original_url", pre=True)
    def validate_url(cls, v):
        if isinstance(v, str):
            v = v.strip()

        if v.endswith("//"):
            raise ValueError("URL cannot end with '//'")
        

        allowed_tlds = [".com", ".ir", ".net"]
        if not any(v.endswith(tld) for tld in allowed_tlds):
            raise ValueError(f"URL must end with one of {allowed_tlds}")
        
        return v

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


