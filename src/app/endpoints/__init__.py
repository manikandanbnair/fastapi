from fastapi import APIRouter
from .user import user_router

all_router = APIRouter()

all_router.include_router(user_router)