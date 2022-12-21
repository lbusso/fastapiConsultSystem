from fastapi import APIRouter
from routers import user_router, auth_router, consult_router, reply_router


api_router = APIRouter()

api_router.include_router(user_router.router)
api_router.include_router(auth_router.router)
api_router.include_router(consult_router.router)
api_router.include_router(reply_router.router)