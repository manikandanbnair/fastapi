
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

        return self._db.get_user(user_id)
    
    def create_user(self, user: User):

        result = self._db.create_user(user)
        if result:
            return user