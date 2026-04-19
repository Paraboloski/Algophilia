import flet as ft
from typing import Optional

class Label(ft.Text):
    def __init__(
        self,
        value: str = "",
        size: int = 14,
        weight: ft.FontWeight = ft.FontWeight.NORMAL,
        color: str = "#FFFFFF",
        text_align: ft.TextAlign = ft.TextAlign.LEFT,
        width: Optional[int] = None,
        italic: bool = False,
        opacity: float = 1.0,
        **kwargs,
    ):
        super().__init__(
            value=value,
            size=size,
            weight=weight,
            color=color,
            text_align=text_align,
            width=width,
            italic=italic,
            opacity=opacity,
            **kwargs,
        )
