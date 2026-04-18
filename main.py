import logging
import asyncio
import flet as ft
from Frontend.src.app import App
from middleware.db import Database
from Backend.api.service import seed
from middleware.config.core.logger import setup_logging

logger = logging.getLogger(__name__)
_listener = setup_logging()


async def bootstrap() -> None:
    try:
        logger.info("Inizializzazione database...")
        init_result = await Database.init_db()
        if init_result.is_err():
            logger.error("Errore DB: %s", init_result.unwrap_err())
            return

        logger.info("Avvio seed dati...")
        await seed.run_seed()
        logger.info("Bootstrap completato")

    except Exception:
        logger.exception("Errore critico durante il bootstrap")
    finally:
        _listener.stop()


async def main(page: ft.Page):
    app = App(page)
    app.run()

    asyncio.create_task(bootstrap())

ft.run(main, assets_dir="frontend/assets")