from pydantic import BaseModel, HttpUrl, validator, Field
from datetime import datetime
from typing import Optional, Literal

class URLCreate(BaseModel):
    original_url: HttpUrl = Field(..., min_length=1)

    @validator("original_url", pre=True)
    def validate_url(cls, v):
        if not isinstance(v, str):
            raise ValueError("Invalid input type")
        url = v.strip()

        # allowed_tlds = [".com", ".ir", ".net"]
        # if not any(url.endswith(tld) for tld in allowed_tlds):
        #     raise ValueError(f"URL must end with one of {allowed_tlds}")
        
        try:
            HttpUrl(url)
        except:
            raise ValueError("Invalid URL format")

        return url

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


