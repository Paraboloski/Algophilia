import flet as ft
from typing import Optional, Callable, Union

class IconBtn(ft.IconButton):
    def __init__(
        self,
        icon: Union[ft.IconData, ft.Control],
        on_click: Optional[Callable] = None,
        icon_color: str = "#BDBDBD",
        icon_size: int = 24,
        visible: bool = True,
        disabled: bool = False,
        tooltip: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            icon=icon,
            on_click=on_click,
            icon_color=icon_color,
            icon_size=icon_size,
            opacity=1.0 if visible else 0.0,
            disabled=disabled or not visible,
            tooltip=tooltip,
            **kwargs,
        )

    def set_visible(self, visible: bool) -> None:
        self.opacity = 1.0 if visible else 0.0
        self.disabled = not visible
