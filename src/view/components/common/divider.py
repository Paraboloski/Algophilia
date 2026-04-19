import flet as ft


class StyledDivider(ft.Divider):
    def __init__(
        self,
        height: int = 10,
        color: str = "#333333",
        thickness: float = 1.0,
        **kwargs,
    ):
        super().__init__(height=height, color=color, thickness=thickness, **kwargs)
