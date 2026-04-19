import logging
import asyncio
import flet as ft
from src.view.app import App
from src.data import Database
from src.api.service import seed
from src.config.env import get_env_int
from src.config import attempt_async, AppError
from src.middleware import setup_logging, notify

setup_logging()
logger = logging.getLogger(__name__)

_ready = asyncio.Event()
_bootstrap_task: asyncio.Task | None = None


async def bootstrap() -> None:
    async def _run():
        logger.info("Inizializzazione database...")
        db_res = await Database.init_db()
        if db_res.is_err():
            return db_res

        logger.info("Avvio seed...")
        await seed.run_seed()
        
        logger.info("Bootstrap completato")
        return db_res

    res = await attempt_async(
        _run(),
        lambda e: AppError(message=f"Critical bootstrap error: {e}")
    )

    if res.is_err():
        error = res.unwrap_err()
        logger.error("Bootstrap Fail: %s", error)
        await notify(f"Errore critico bootstrap\n`{error}`", level="critical")
    
    _ready.set()


async def main(page: ft.Page) -> None:
    global _bootstrap_task
    if _bootstrap_task is None:
        _bootstrap_task = asyncio.create_task(bootstrap())
    await _ready.wait()
    App(page).run()


if __name__ == "__main__":
    ft.run(main, assets_dir="frontend/assets")