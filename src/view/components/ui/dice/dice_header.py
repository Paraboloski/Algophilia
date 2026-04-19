import flet as ft
from typing import List, cast
from src.view.components.common import Label, Row, Container

class ColumnHeaders(Row):
    def __init__(
        self,
        qty_label: str = "QTÀ",
        sides_label: str = "DADO",
        qty_width: int = 110,
        sides_width: int = 110,
        spacer_width: int = 80,
        color: str = "#BDBDBD",
    ):
        super().__init__(
            controls=cast(List[ft.Control], [
                Label(
                    value=qty_label,
                    size=10,
                    weight=ft.FontWeight.BOLD,
                    color=color,
                    width=qty_width,
                    text_align=ft.TextAlign.CENTER,
                ),
                Label(
                    value=sides_label,
                    size=10,
                    weight=ft.FontWeight.BOLD,
                    color=color,
                    width=sides_width,
                    text_align=ft.TextAlign.CENTER,
                ),
                Container(width=spacer_width),
            ]),
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )