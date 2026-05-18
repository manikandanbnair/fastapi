from typing import List

from sqlalchemy import Row, select, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.models.user_model import User
from app.models.user_table import user_table


class PostgresService:
    def __init__(self, db_name: str, user: str, password: str, host: str, port: int):
        self._databaseurl = (
            f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
        )

        self.engine = create_async_engine(self._databaseurl, echo=False)

        self.session_factory = async_sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def get_session(self):
        async with self.session_factory() as session:
            yield session

    async def close(self):
        await self.engine.dispose()

    async def test_connection(self) -> bool:
        try:
            async with self.engine.begin() as conn:
                await conn.execute(text("SELECT 1"))
                return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False

    async def execute_query(self, query: str):
        try:
            async with self.engine.begin() as conn:
                await conn.execute(query)
        except Exception as e:
            print(f"Query execution failed: {e}")
            return None

    async def fetch_query(self, query: str):
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(query)
                return [dict(row) for row in result.mappings().all()]
        except Exception as e:
            print(f"Query execution failed: {e}")
            return None

    async def fetch_one_query(self, query: str):
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(text(query))
                return result.fetchone()
        except Exception as e:
            print(f"Query execution failed: {e}")
            return None

    async def get_user(self, user_id: int):
        query = select(
            user_table.c.id,
            user_table.c.username,
            user_table.c.email,
            user_table.c.age,
            user_table.c.is_active,
        )
        if user_id:
            query = query.where(user_table.c.id == user_id)
        result = await self.fetch_query(query)
        return result

    async def create_user(self, user_data: User):
        query = user_table.insert().values(
            username=user_data.username,
            email=user_data.email,
            age=user_data.age,
            is_active=user_data.is_active,
        )
        await self.execute_query(query)
        return True
