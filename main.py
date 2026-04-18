import logging
import asyncio
import flet as ft
from Frontend.src.app import App
from middleware.db import Database
from Backend.api.service import seed
from middleware.config.core.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

_ready = asyncio.Event()
_bootstrap_task: asyncio.Task | None = None


async def bootstrap() -> None:
    try:
        logger.info("Inizializzazione database...")
        init_result = await Database.init_db()
        if init_result.is_err():
            logger.error("Errore DB: %s", init_result.unwrap_err())
            return

        logger.info("Avvio seed...")
        await seed.run_seed()
        logger.info("Bootstrap completato")

    except Exception:
        logger.exception("Errore critico durante il bootstrap")

    finally:
        _ready.set()


async def main(page: ft.Page) -> None:
    global _bootstrap_task
    if _bootstrap_task is None:
        _bootstrap_task = asyncio.create_task(bootstrap())
    await _ready.wait()
    App(page).run()


ft.run(main, assets_dir="frontend/assets")