
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