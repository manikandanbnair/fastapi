from dependency_injector import containers, providers

from app.service.postgres import PostgresService
from app.service.user_service import UserService
from app.settings import Settings


class Service(containers.DeclarativeContainer):

    settings = providers.Singleton(Settings)

    db_service = providers.Singleton(
        PostgresService,
        db_name=settings.db.db_name,
        user=settings.db.user,
        password=settings.db.password,
        host=settings.db.host,
        port=settings.db.port,
    )


class Containers(containers.DeclarativeContainer):
    config = providers.Configuration()

    service: providers.Container[Service] = providers.Container(
        Service, config = config
    )

    user_service: providers.Singleton[UserService] = providers.Singleton(
        UserService,
        db = service.db_service
    )