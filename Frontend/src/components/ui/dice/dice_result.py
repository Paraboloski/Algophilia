import flet as ft
from typing import Callable, List, cast, Optional
from Frontend.src.components.common import Label

class ResultOverlay(ft.Container):
    def __init__(
        self,
        on_exit: Optional[Callable] = None,
        label_result: str = "RISULTATO",
        label_continue: str = "TOCCA PER CHIUDERE",
        bgcolor: str = "rgba(24, 24, 24, 0.7)",
        blur_sigma: float = 5.0,
        accent_color: str = "#FFD700",
        muted_color: str = "#BDBDBD",
    ):
        self._on_exit = on_exit
 
        self._total_text = Label(
            value="",
            size=100,
            weight=ft.FontWeight.W_900,
            color=accent_color,
        )
 
        super().__init__(
            content=ft.Column(
                controls=cast(List[ft.Control], [
                    Label(
                        value=label_result,
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color=accent_color,
                    ),
                    self._total_text,
                    ft.Container(height=20),
                    Label(
                        value=label_continue,
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=muted_color,
                    ),
                ]),
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=bgcolor,
            blur=ft.Blur(blur_sigma, blur_sigma),
            expand=True,
            opacity=0,
            animate_opacity=400,
            visible=False,
            on_click=self._handle_click,
        )
 
    def set_on_exit(self, cb: Callable) -> None: self._on_exit = cb
 
    def prepare(self, total: int) -> None:
        self._total_text.value = str(total)
        self.visible = True
        self.opacity = 0
 
    def reveal(self) -> None:
        self.opacity = 1.0
 
    def dismiss(self) -> None: self.opacity = 0.0
 
    def hide(self) -> None: self.visible = False
 
    @property
    def total_text(self) -> ft.Text: return self._total_text
 
    async def _handle_click(self, e) -> None:
        if self._on_exit: await self._on_exit(e)
 