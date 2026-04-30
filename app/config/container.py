from dependency_injector import containers, providers

from app.utils import Directory
from app.config.settings import settings
from app.data import Repository, Database
from app.events import Telegram, Logger, Worker


class DependencyInjectorContainer(containers.DeclarativeContainer):
    worker = providers.Singleton(Worker)
    logger = providers.Singleton(
        Logger,
        directory=Directory(settings.log_dir),
        worker=worker,
    )

    telegram = providers.Singleton(
        Telegram,
        token=settings.telegram_token,
        chat_id=settings.telegram_chat_id,
    )

    database = providers.Singleton(
        Database,
        logger=logger,
        schema_path=settings.schema_path,
        url=settings.database_url,
        seed_paths=settings.seed_files,
    )

    repository = providers.Singleton(
        Repository,
        database=database,
        logger=logger,
    )