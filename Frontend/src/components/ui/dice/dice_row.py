import flet as ft
from typing import Callable, List, cast
from Frontend.src.components.common import IconBtn


class DiceSetRow(ft.Row):
    QTY_OPTIONS = [str(i) for i in range(1, 11)]
    SIDES_OPTIONS = [str(s) for s in [4, 6, 8, 10, 12, 20, 100]]

    def __init__(
        self,
        on_delete: Callable[["DiceSetRow"], None],
        on_add: Callable[[None], None],
        show_add: bool = False,
        default_qty: str = "1",
        default_sides: str = "20",
    ):
        super().__init__()
        self.on_delete = on_delete
        self.on_add = on_add

        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 10
        self.alignment = ft.MainAxisAlignment.CENTER

        self.qty_dropdown = ft.Dropdown(
            value=default_qty,
            width=110,
            options=[ft.DropdownOption(v) for v in self.QTY_OPTIONS],
            text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
        )

        self.sides_dropdown = ft.Dropdown(
            value=default_sides,
            width=110,
            options=[ft.DropdownOption(v) for v in self.SIDES_OPTIONS],
            text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
        )

        self.add_btn = IconBtn(
            icon=ft.Icons.ADD_CIRCLE,
            icon_color="#FFD700",
            icon_size=28,
            on_click=lambda _: self.on_add(None),
            visible=show_add,
        )

        self.delete_btn = IconBtn(
            icon=ft.Icons.DELETE_OUTLINE,
            icon_color="#BDBDBD",
            icon_size=24,
            on_click=lambda _: self.on_delete(self),
        )

        self.controls = cast(
            List[ft.Control],
            [self.qty_dropdown, self.sides_dropdown, self.add_btn, self.delete_btn],
        )

    @property
    def qty(self) -> int: return int(self.qty_dropdown.value or "1")

    @property
    def sides(self) -> int: return int(self.sides_dropdown.value or "20")

    def set_add_visible(self, visible: bool) -> None: self.add_btn.set_visible(visible)