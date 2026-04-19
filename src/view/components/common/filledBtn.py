import flet as ft
from typing import Optional, Callable

class FilledBtn(ft.FilledButton):
    def __init__(
        self,
        text: str,
        on_click: Optional[Callable] = None,
        width: int = 220,
        height: int = 50,
        bgcolor: str = "#FFD700",
        color: str = "#121212",
        border_radius: int = 8,
        disabled: bool = False,
        **kwargs,
    ):
        super().__init__(
            text,
            on_click=on_click,
            width=width,
            height=height,
            disabled=disabled,
            style=ft.ButtonStyle(
                bgcolor=bgcolor,
                color=color,
                shape=ft.RoundedRectangleBorder(radius=border_radius),
            ),
            **kwargs,
        )
