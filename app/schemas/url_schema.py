from pydantic import BaseModel, HttpUrl, validator

class CreateLinkSchema(BaseModel):
    original_url: HttpUrl

    @validator("original_url", pre=True)
    def validate_url(cls, v):
        url = v.strip()

        allowed_tlds = [".com", ".ir", ".net"]
        if not any(url.endswith(tld) for tld in allowed_tlds):
            raise ValueError(f"URL must end with one of {allowed_tlds}")
        
        try:
            HttpUrl.validate(url)
        except:
            raise ValueError("Invalid URL format")

        return url



