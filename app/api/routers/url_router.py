from fastapi import APIRouter, Depends, HTTPException, status
from app.services.url_service import URLService
from app.api.schemas.url_schema import URLCreate, URLResponse, URLListSchema
from app.api.schemas.request_schema import ResponseSchema, ErrorSchema
from app.api.dependencies import get_url_service
from app.models import ShortenedURL
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/urls", tags=["ShortenedURL"])

@router.post("/", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
async def create_url(payload: URLCreate, service: URLService = Depends(get_url_service)):
    try:
        shortened_url = service.create(str(payload.original_url))
        return URLResponse(
            status="success",
            id=shortened_url.id,
            original_url=shortened_url.original_url,
            short_code=shortened_url.short_code,
            created_at=shortened_url.created_at,
            expires_at=shortened_url.expires_at,
            message=None
        )
    except ValueError as e:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=URLResponse(
                    status="failure",
                    message=str(e)
                ).model_dump()
            )
    # except Exception as e:
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail=URLResponse(
    #             status="failure",
    #             message="An unexpected error occurred."
    #         ).model_dump()
    #     )

@router.get("/u/{code}", response_model=URLResponse)
async def get_url(code: str, service: URLService = Depends(get_url_service)):
    try:
        original_url = service.get_by_code(code)
        # URLResponse(
        #     status="success",
        #     id=original_url.id,
        #     original_url=original_url.original_url,
        #     short_code=original_url.short_code,
        #     created_at=original_url.created_at,
        #     expires_at=original_url.expires_at,
        #     message=None
        # )
        return RedirectResponse(url=original_url.original_url, status_code=status.HTTP_302_FOUND)
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=URLResponse(
                status="failure",
                message=str(e)
            ).model_dump()
        )


@router.get('/', response_model=ResponseSchema[list[URLListSchema]])
def list_urls(service: URLService = Depends(get_url_service)):
    ...


@router.delete('/{short_code}', response_model=ResponseSchema[str])
def delete_url(short_code:str, service: URLService = Depends(get_url_service)):
    ...
               
               