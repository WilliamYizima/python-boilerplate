from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

health_route = APIRouter(
    prefix="/api",
    tags=["status"],
    # dependencies=[Depends(get_token_header)],to auth
    responses={404: {"description": "Not found"}},
)


@health_route.get("/health")
async def health():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success": True})
