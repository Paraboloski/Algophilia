import flet as ft
from app.config import settings
from app.core.exception import Error
from app.view.fallback import Fallback
from app.domain.data.database import Database
from app.services.load_registry import load_all

async def init_app() -> Database:
    load_all()

    db = Database(
        db=settings.DATABASE_PATH, 
        schema=settings.SCHEMA_PATH
    )

    (await db.connect()).unwrap()
    (await db.seed()).unwrap()

    return db

def main(page: ft.Page) -> None:

    async def start() -> None:
        try:
            db = await init_app()
            page.session.store.set("db", db)
        except Error as e:
            Fallback(page, "Errore applicativo", str(e))
        except Exception as e:
            Fallback(page, "Errore critico", str(e))

    page.run_task(start)

if __name__ == "__main__":
    ft.run(main, assets_dir="app/assets")