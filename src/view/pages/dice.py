import asyncio
import flet as ft
from result import Err
from src.lib import roll
from typing import Optional, Callable, List, Tuple, cast
from src.view.components import ResultOverlay, DiceConfigPanel, DiceAnimationArea

class DiceRoller(ft.Container):
    def __init__(self, on_close: Optional[Callable] = None):
        super().__init__()
        self.expand = True
        self.bgcolor = "#181818"
        self.padding = ft.Padding(top=80, left=20, right=20, bottom=20)
        self.alignment = ft.Alignment(x=0, y=0)
        self.on_close = on_close

        self.config_panel = DiceConfigPanel(on_roll=self.roll_action)
        self.animation_area = DiceAnimationArea()
        self.result_overlay = ResultOverlay(on_exit=self.handle_exit)
 

    def did_mount(self):
        main_layout = ft.Column(
            controls=cast(List[ft.Control], [
                self.config_panel,
                self.animation_area,
            ]),
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,
            expand=True,
        )
 
        self.content = ft.Stack(controls=cast(List[ft.Control], [main_layout, self.result_overlay]))
        self.update()
 
    async def roll_action(self, _e) -> None:
        self.config_panel.set_disabled(True)
        self.animation_area.clear()
        self.result_overlay.hide()
        self.update()
 
        all_rolls: List[Tuple[int, int]] = []
        total = self.config_panel.bonus
 
        for row in self.config_panel.dice_rows:
            result = roll(quantity=row.qty, sides=row.sides, bonus=0)
            if isinstance(result, Err): continue
            res = result.unwrap()
            total += sum(res["rolls"])
            all_rolls.extend((v, row.sides) for v in res["rolls"])
 
        self.animation_area.populate(all_rolls)
        self.update()
 
        await asyncio.sleep(0.1)
        await self.animation_area.animate(self.update)
 
        self.result_overlay.prepare(total)
        self.update()
        await asyncio.sleep(0.5)
        self.result_overlay.reveal()
        self.update()
 
    async def handle_exit(self, _e) -> None:
        self.result_overlay.dismiss()
        self.update()
 
        await asyncio.sleep(0.4)
 
        self.result_overlay.hide()
        self.config_panel.set_disabled(False)
        self.animation_area.clear()
        self.update()
 
        if self.on_close:
            result = self.on_close()
            if asyncio.iscoroutine(result): await result
 
 