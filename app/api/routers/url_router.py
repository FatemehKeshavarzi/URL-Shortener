from fastapi import APIRouter, Depends, HTTPException, status
from app.services.url_service import URLService
from app.api.schemas.url_schema import URLCreate, URLResponse, URLListSchema
from app.api.schemas.request_schema import ResponseSchema, ErrorSchema
from app.api.dependencies import get_url_service
from app.models import ShortenedURL
from fastapi.responses import RedirectResponse, JSONResponse

router = APIRouter(prefix="/urls", tags=["ShortenedURL"])

@router.post("/", response_model=ResponseSchema[URLResponse], status_code=status.HTTP_201_CREATED)
async def create_url(payload: URLCreate, service: URLService = Depends(get_url_service)):
    try:
        shortened_url = service.create(str(payload.original_url))
        return ResponseSchema(
            data=URLResponse(
                id=shortened_url.id,
                original_url=shortened_url.original_url,
                short_code=shortened_url.short_code,
                created_at=shortened_url.created_at,
                expires_at=shortened_url.expires_at,
            )
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=ErrorSchema(message=str(e)).model_dump())

@router.get("/u/{code}", response_model=ResponseSchema[URLResponse])
async def get_url(code: str, service: URLService = Depends(get_url_service)):
    try:
        original_url = service.get_by_code(code)
        return RedirectResponse(url=original_url.original_url, status_code=status.HTTP_302_FOUND)
        
    except ValueError as e:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=ErrorSchema(message=str(e)).model_dump())


@router.get('/', response_model=ResponseSchema[list[ShortenedURL]])
def list_urls(service: URLService = Depends(get_url_service)):
    urls = service.list_urls()
    return ResponseSchema(data=urls)


@router.delete('/{code}', response_model=ResponseSchema[str])
def delete_url(code:str, service: URLService = Depends(get_url_service)):
    try:
        service.delete_by_code(code=code)
        return ResponseSchema(data='deleted')
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=ErrorSchema(message=str(e)).model_dump())

               
               