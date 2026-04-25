import flet as ft
from pathlib import Path
from app.core.result import Err
from app.data.database import Database
from app.core.exception import AppError
from app.data.seeder import seed_database
from app.services.registry import load_all
from app.config import logger, settings, Panic
from app.view.components.ui.toast import ToastManager
from app.notification import ToastNotifier, TelegramNotifier

logger.init(Path(__file__).parent)

logger.subscribe(TelegramNotifier(
    token=settings.TELEGRAM_TOKEN,
    id=settings.TELEGRAM_CHAT_ID
).on_log)

class AppContext:
    def __init__(self, page: ft.Page):
        self.page = page
        self.toast = ToastManager(page, 20)

async def init_app() -> Database:
    load_all()

    db = Database(
        db=settings.DATABASE_PATH,
        schema=settings.SCHEMA_PATH
    )

    _conn = await db.connect()
    if isinstance(_conn, Err):
        Panic._panic(f"Impossibile connettersi al database: {_conn.error}")

    _seed = await seed_database(db)
    if isinstance(_seed, Err):
        Panic._panic(f"Inizializzazione dati (seeding) fallita: {_seed.error}")

    return db


def main(page: ft.Page) -> None:
    ctx = AppContext(page)
    toast_notifier = ToastNotifier(ctx.toast)
    logger.subscribe(toast_notifier.on_log)

    async def start() -> None:
        try:
            db = await init_app()
            page.session.store.set("db", db)
            logger.info("init OK")
        except AppError as e:
            logger.error(f"init NOT OK: {str(e)}")

    page.run_task(start)

    def close(_):
        logger.unsubscribe(toast_notifier.on_log)
        logger.shutdown()

    page.on_close = close


if __name__ == "__main__":
    ft.run(main, assets_dir="app/assets")

