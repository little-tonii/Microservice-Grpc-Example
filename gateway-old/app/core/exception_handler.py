from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import grpc
from starlette import status
from grpc.aio import AioRpcError
from app.schemas.responses.error_schema_response import ErrorResponse, ErrorsResponse


async def handle_grpc_exception(exception: AioRpcError):
    status_code = exception.code()
    message = exception.details()
    if status_code == grpc.StatusCode.NOT_FOUND:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)


async def http_exception_handler(request: Request, exc: HTTPException):
    message = exc.detail
    return JSONResponse(
        status_code=exc.status_code, 
        content=ErrorResponse(message=message).model_dump()
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    messages = []
    for error in exc.errors():
        head_removed = str(error["msg"]).split(", ")[1]
        messages.append(head_removed)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorsResponse(messages=messages).model_dump()
    )

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500, 
        content=ErrorResponse(message=str(exc)).model_dump()
    )