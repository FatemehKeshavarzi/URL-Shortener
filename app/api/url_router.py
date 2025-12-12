from fastapi import APIRouter, Depends, HTTPException, status
from services.url_service import URLService
from schemas.url_schema import URLResponse, URLCreate
from api.dependencies import get_url_service

router = APIRouter(prefix="/urls", tags=["ShortenedURL"])

@router.post("/", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
async def create_project(payload: URLCreate, service: URLService = Depends(get_url_service)):
    try:
        shortened_url = service.create(payload.original_url)
        return shortened_url
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{short_code}", response_model=URLResponse)
async def get_project(short_code: str, service: URLService = Depends(get_url_service)):
    original_link = service.get_by_code(short_code)
    if not original_link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="link not found")
    return original_link
