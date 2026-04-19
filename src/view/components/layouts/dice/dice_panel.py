import flet as ft
from typing import Callable, List, cast
from src.view.components import DiceSetRow, ColumnHeaders, Label, FilledBtn, NumberField, StyledDivider, Column, Row

class DiceConfigPanel(Column):
    MAX_ROWS = 4
 
    def __init__(
        self,
        on_roll: Callable,
        title: str = "ALGOPHILIA",
        roll_label: str = "TIRA I DADI",
        bonus_label: str = "Bonus",
        accent_color: str = "#FFD700",
    ):
        self._on_roll = on_roll
 
        self.rows_container = Column(
            spacing=5,
            animate_opacity=300,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
 
        self.bonus_field = NumberField(label=bonus_label, value="0")
 
        self.roll_btn = FilledBtn(
            text=roll_label,
            on_click=on_roll,
            bgcolor=accent_color,
            color="#121212",
            width=230,
        )
 
        super().__init__(
            controls=cast(List[ft.Control], [
                Label(
                    value=title,
                    size=12,
                    weight=ft.FontWeight.BOLD,
                    color=accent_color,
                ),
                StyledDivider(),
                ColumnHeaders(),
                self.rows_container,
                Row(
                    controls=cast(List[ft.Control], [self.roll_btn, self.bonus_field]),
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                ),
            ]),
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
 
    def did_mount(self) -> None:
        if not self.rows_container.controls: self._add_row_silent()
 
    def _add_row_silent(self) -> None:
        new_row = DiceSetRow(
            on_delete=self.remove_row,
            on_add=self.add_row,
            show_add=True,
        )
        self.rows_container.controls.append(new_row)
 
    def add_row(self, _e=None) -> None:
        count = len(self.rows_container.controls)
        if count >= self.MAX_ROWS: return
 
        for row in cast(List[DiceSetRow], self.rows_container.controls):  row.set_add_visible(False)
 
        new_row = DiceSetRow(
            on_delete=self.remove_row,
            on_add=self.add_row,
            show_add=(count + 1 < self.MAX_ROWS),
        )
        self.rows_container.controls.append(new_row)
 
        if self.page: self.update()
 
    def remove_row(self, row: DiceSetRow) -> None:
        if len(self.rows_container.controls) <= 1: return
        
        self.rows_container.controls.remove(row)
        if len(self.rows_container.controls) < self.MAX_ROWS:
            last = cast(DiceSetRow, self.rows_container.controls[-1])
            last.set_add_visible(True)
 
        if self.page: self.update()
 
    def set_disabled(self, disabled: bool) -> None:
        self.rows_container.disabled = disabled
        self.roll_btn.disabled = disabled
        self.bonus_field.disabled = disabled
 
    @property
    def bonus(self) -> int:
        try:
            return int(self.bonus_field.value or "0")
        except ValueError:
            return 0
 
    @property
    def dice_rows(self) -> List[DiceSetRow]:
        return cast(List[DiceSetRow], self.rows_container.controls)