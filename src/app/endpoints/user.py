# routers/user.py

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.container import Containers
from app.models.user_model import User


user_router = APIRouter()


@user_router.get("/user")
async def get_user():

    response = await Containers.user_service().get_user()

    return JSONResponse(status_code= status.HTTP_200_OK if response else status.HTTP_404_NOT_FOUND,
                        content={"users": response})

@user_router.get("/db-health")
async def db_health_check():

    response = await Containers.user_service().db_health_check()

    return JSONResponse(status_code= status.HTTP_200_OK if response else status.HTTP_503_SERVICE_UNAVAILABLE,
                        content={"db_status": response})

@user_router.post("/user")
async def create_user(user: User):

    response = await Containers.user_service().create_user(user)

    return JSONResponse(status_code= status.HTTP_201_CREATED if response else status.HTTP_400_BAD_REQUEST,
                        content={"user": response})