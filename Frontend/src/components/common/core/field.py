import flet as ft
from typing import Optional

class NumberField(ft.TextField):
    def __init__(
        self,
        label: str = "",
        value: str = "0",
        width: int = 80,
        border_color: str = "#333333",
        focused_border_color: str = "#FFD700",
        text_align: ft.TextAlign = ft.TextAlign.CENTER,
        disabled: bool = False,
        hint_text: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            label=label,
            value=value,
            width=width,
            border_color=border_color,
            focused_border_color=focused_border_color,
            text_align=text_align,
            keyboard_type=ft.KeyboardType.NUMBER,
            disabled=disabled,
            hint_text=hint_text,
            **kwargs,
        )
