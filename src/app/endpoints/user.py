# routers/user.py

from fastapi import APIRouter

from app.container import Containers


user_router = APIRouter()


@user_router.get("/user")
async def get_user():

    response = await Containers().user_service.get_user()

    return response