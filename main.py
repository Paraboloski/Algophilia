import sys
import flet as ft
from app.view.app import App
from typing import Any, Never
from app.utils import AppError
from app.config import Container


def panic(err: Any) -> Never:
    print(f"panic: {err}", file=sys.stderr)
    sys.exit(1)


class Session:
    def __init__(self, page: ft.Page, container: Container, app: App) -> None:
        self.app = app
        self.page = page
        self.container = container

    async def bootstrap(self) -> None:
        logger = self.container.logger()
        logger.subscribe(self.container.telegram().send)

        result = await self.container.database().connect()
        if result.is_err():
            error = result.unwrap_err()
            logger.error(f"Bootstrap: Errore inizializzazione DB | {error}")
            panic(error)

    async def shutdown(self) -> None:
        result = await self.container.database().disconnect()
        if result.is_err():
            self.container.logger().error(f"Shutdown: {result.unwrap_err()}")

        self.container.worker().shutdown()
        self.container.logger()._directory.rmdir()

    def cleanup(self) -> None:
        self.page.on_close = None
        self.page.on_disconnect = None
        self.app.close()
        self.page.run_task(self.shutdown)


async def main(page: ft.Page) -> None:
    container = Container()
    app = App(page, container)
    session = Session(page, container, app)

    page.on_close = session.cleanup
    page.on_disconnect = session.cleanup

    try:
        await app.build()
        await session.bootstrap()
    except AppError as e:
        panic(e)


if __name__ == "__main__":
    ft.run(main, assets_dir="app/assets")
