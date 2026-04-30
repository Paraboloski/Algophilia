import flet as ft
from app.config import Container
from app.view.style import settings
from app.view.components.common import Image
from app.view.components.ui.toast import ToastManager


class App:
    def __init__(self, page: ft.Page, container: Container):
        self.page = page
        self.container = container
        self.toast: ToastManager | None = None
        self._device_width = settings._main_width
        self._device_height = settings._main_height

        self.page.padding = 0
        self.page.title = settings._app_name
        self.page.bgcolor = settings._main_colors["bg_dark"]

        self.page.fonts = {
            name: str(path) for name, path in settings._main_fonts.items()
        }

    def ready(self) -> None:
        self.page.window.frameless = True
        self.page.window.resizable = False
        self.page.window.maximizable = False
        self.page.window.title_bar_hidden = False
        self.page.window.width = self._device_width
        self.page.window.height = self._device_height
        self.page.window.min_width = self._device_width
        self.page.window.max_width = self._device_width
        self.page.window.min_height = self._device_height
        self.page.window.max_height = self._device_height
        self.page.window.aspect_ratio = self._device_width / self._device_height

    async def build(self):
        await self.page.window.wait_until_ready_to_show()
        self.ready()
        await self.page.window.center()

        content = ft.Column(
            controls=[
                ft.Text(
                    settings._app_name,
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color=settings._main_colors["bg_light"],
                    font_family="cinzel_bold",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

        self.toast = ToastManager(
            page=self.page,
            logger=self.container.logger(),
            safe_area_top=40,
        )

        self.page.add(
            ft.Stack(
                controls=[
                    ft.Container(
                        image=Image(
                            path=settings._main_images["bg_fallback"],
                            fit=ft.BoxFit.COVER,
                            opacity=0.3,
                        ),
                        expand=True,
                    ),
                    ft.Container(
                        content=content,
                        alignment=ft.alignment.Alignment(0, 0),
                        expand=True,
                    ),
                ],
                expand=True,
                fit=ft.StackFit.EXPAND,
                alignment=ft.alignment.Alignment(0, 0),
            )
        )

        self.toast.info("TEST 1")
        self.toast.warning("TEST 2")
        self.toast.error("TEST 3")
        self.page.update()

    def close(self) -> None:
        if self.toast is not None:
            self.toast.close()
