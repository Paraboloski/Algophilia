import flet as ft
from typing import Optional
from src.config import attempt

class NumberField(ft.TextField):
    def __init__(
        self,
        label: str = "",
        value: str = "0",
        width: int = 80,
        border_color: str = "white",
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
            on_focus=self._handle_focus,
            on_change=self._handle_change,
            **kwargs,
        )

    def _handle_focus(self, e):
        self.selection = ft.TextSelection(0, len(str(self.value)))
        self.update()

    def _handle_change(self, e):
        val = self.value
        if not val:
            self.value = "0"
        elif len(val) > 1 and val.startswith("0"):
            self.value = val.lstrip("0")
            if not self.value:
                self.value = "0"
        
        try:
            if int(self.value) > 999: self.value = "999"
        except ValueError:
            pass 

        self.update()
