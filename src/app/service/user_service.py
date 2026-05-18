
from app.models.user_model import User
from app.service.postgres import PostgresService


class UserService:
    def __init__(
            self,
            db: PostgresService
            ):
        self._db: PostgresService = db

    def db_health_check(self) -> bool:
        status = self._db.test_connection()
        return status
    
    def get_user(self, user_id: int = None):

        result = self._db.get_user(user_id)
        print(f"UserService.get_user: Retrieved user data: {result}")
        return result
    
    async def create_user(self, user: User):

        result = await self._db.create_user(user)
        if result:
            return user