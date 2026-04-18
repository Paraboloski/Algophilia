import logging
import asyncio
import flet as ft
from middleware.db import Database
from Backend.api.service import seed
from middleware.config.core.logger import setup_logging
from Frontend.src.views import DiceRoller

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


async def main(page: ft.Page) -> None:
    page.title = "Algophilia"
    page.bgcolor = "#181818"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.fonts = {"Cinzel": "fonts/Cinzel-Regular.ttf"}
    page.theme = ft.Theme(font_family="Cinzel")

    page.add(DiceRoller())
    page.update()

    asyncio.create_task(bootstrap())


ft.run(main, assets_dir="frontend/assets")