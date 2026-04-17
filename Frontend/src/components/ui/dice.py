import asyncio
import random
import flet as ft
import flet.canvas as cv
from typing import Optional, Callable, List, cast, TypedDict

try:
    from Backend.util.dice import roll, DiceRollResult
except ImportError:
    # type: ignore[no-redef]
    class DiceRollResult(TypedDict):
        total: int
        rolls: List[int]
        expression: str
        bonus: int

    # type: ignore[misc]
    def roll(quantity: int, sides: int, bonus: int = 0) -> DiceRollResult:
        rolls = [random.randint(1, sides) for _ in range(quantity)]
        return DiceRollResult(
            total=sum(rolls) + bonus,
            rolls=rolls,
            expression=f"{quantity}d{sides}",
            bonus=bonus,
        )


class DiceSetRow(ft.Row):
    def __init__(self, on_delete: Callable, on_add: Callable, show_add: bool = False):
        super().__init__()
        self.spacing = 10
        self.on_add = on_add
        self.on_delete = on_delete
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        self.qty_dropdown = ft.Dropdown(
            value="1", width=90,
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
        )

        self.sides_dropdown = ft.Dropdown(
            value="20", width=100,
            options=[ft.dropdown.Option(str(s))
                     for s in [4, 6, 8, 10, 12, 20, 100]],
            text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
        )

        self.delete_btn = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE, icon_color="#BDBDBD", icon_size=24,
            on_click=lambda _: self.on_delete(self),
        )

        self.add_btn = ft.IconButton(
            icon=ft.Icons.ADD_CIRCLE, icon_color="#FFD700", icon_size=28,
            on_click=lambda _: self.on_add(None),
            opacity=1 if show_add else 0,
            disabled=not show_add,
        )

        self.controls = [self.qty_dropdown,
                         self.sides_dropdown, self.add_btn, self.delete_btn]


class DiceRoller(ft.Container):
    POLYGONS = {
        4:  [[50, 10], [90, 85], [10, 85]],
        6:  [[15, 15], [85, 15], [85, 85], [15, 85]],
        8:  [[50, 5],  [90, 50], [50, 95], [10, 50]],
        10: [[50, 5],  [90, 40], [50, 95], [10, 40]],
        12: [[50, 5],  [90, 35], [75, 90], [25, 90], [10, 35]],
        20: [[50, 5],  [90, 25], [90, 75], [50, 95], [10, 75], [10, 25]],
        100: "circle",
    }

    DICE_COLORS = {
        4: "#4CAF50", 6: "#2196F3", 8: "#9C27B0",  10: "#E91E63",
        12: "#F44336", 20: "#FF9800", 100: "#795548",
    }

    def __init__(self, on_close: Optional[Callable] = None):
        super().__init__()
        self.expand = True
        self.bgcolor = "#181818"
        self.padding = ft.Padding(top=80, left=20, right=20, bottom=20)
        self.on_close = on_close
        self.alignment = ft.Alignment(x=0, y=0)

        self.dice_rows_container = ft.Column(
            spacing=5,
            animate_opacity=300,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.dice_area = ft.Stack(height=250, width=350)

        self.bonus_input = ft.TextField(
            label="Bonus", value="0", width=80,
            text_align=ft.TextAlign.CENTER,
            keyboard_type=ft.KeyboardType.NUMBER,
            border_color="#333333",
            focused_border_color="#FFD700",
        )

        self.roll_btn = ft.FilledButton(
            "TIRA I DADI",
            on_click=self.roll_action,
            width=220, height=50,
            style=ft.ButtonStyle(
                bgcolor="#FFD700", color="#121212",
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )

        self.total_text = ft.Text(
            "", size=100, weight=ft.FontWeight.W_900, color="#FFD700")
        self.continue_text = ft.Text(
            "TOCCA PER CHIUDERE", size=14, weight=ft.FontWeight.BOLD, color="#BDBDBD")

        self.result_overlay = ft.Container(
            content=ft.Column(
                [
                    ft.Text("RISULTATO", size=12,
                            weight=ft.FontWeight.BOLD, color="#FFD700"),
                    self.total_text,
                    ft.Container(height=20),
                    self.continue_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="rgba(24, 24, 24, 0.7)",
            blur=ft.Blur(5, 5),
            expand=True,
            opacity=0,
            animate_opacity=400,
            visible=False,
            on_click=self.handle_exit,
        )

    def did_mount(self):
        self._haptic = ft.HapticFeedback()
        if self.page is not None:
            self.page.overlay.append(self._haptic)
            self.page.update()

        if not self.dice_rows_container.controls:
            self.add_dice_row(None)

        self.main_layout = ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("ALGOPHILIA", size=12,
                                weight=ft.FontWeight.BOLD, color="#FFD700"),
                        ft.Divider(height=10, color="#333333"),
                        ft.Row(
                            [
                                ft.Text("QTÀ",  size=10, weight=ft.FontWeight.BOLD,
                                        color="#BDBDBD", width=90,  text_align=ft.TextAlign.CENTER),
                                ft.Text("DADO", size=10, weight=ft.FontWeight.BOLD,
                                        color="#BDBDBD", width=100, text_align=ft.TextAlign.CENTER),
                                ft.Container(width=80),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        ),
                        self.dice_rows_container,
                        ft.Row(
                            [self.roll_btn, self.bonus_input],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                ),
                self.dice_area,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,
            expand=True,
        )

        self.content = ft.Stack([self.main_layout, self.result_overlay])
        self.update()

    def add_dice_row(self, e):
        count = len(self.dice_rows_container.controls)
        if count < 4:
            for row in cast(List[DiceSetRow], self.dice_rows_container.controls):
                row.add_btn.opacity = 0
                row.add_btn.disabled = True
            new_row = DiceSetRow(on_delete=self.remove_dice_row,
                                 on_add=self.add_dice_row, show_add=True)
            self.dice_rows_container.controls.append(new_row)
            if len(self.dice_rows_container.controls) == 4:
                new_row.add_btn.opacity = 0
                new_row.add_btn.disabled = True
            if self.page:
                self.update()

    def remove_dice_row(self, row):
        if len(self.dice_rows_container.controls) > 1:
            self.dice_rows_container.controls.remove(row)
            if len(self.dice_rows_container.controls) < 4:
                last_row = cast(
                    DiceSetRow, self.dice_rows_container.controls[-1])
                last_row.add_btn.opacity = 1
                last_row.add_btn.disabled = False
            self.update()

    async def roll_action(self, e):
        self.roll_btn.disabled = True
        self.dice_area.controls.clear()
        self.result_overlay.opacity = 0
        self.bonus_input.disabled = True
        self.result_overlay.visible = False
        self.dice_rows_container.disabled = True

        self.update()

        dice_to_animate = []
        final_total = int(self.bonus_input.value or "0")

        for row in cast(List[DiceSetRow], self.dice_rows_container.controls):
            qty = int(row.qty_dropdown.value or "1")
            sides = int(row.sides_dropdown.value or "20")
            res = roll(quantity=qty, sides=sides, bonus=0)
            final_total += sum(res["rolls"])

            color = self.DICE_COLORS.get(sides, "#FFD700")
            poly_points = self.POLYGONS.get(sides)

            for val in res["rolls"]:
                cp = cv.Canvas(width=70, height=70)
                if poly_points == "circle":
                    cp.shapes.append(
                        cv.Circle(35, 35, 30, ft.Paint(
                            color=color, style=ft.PaintingStyle.FILL))
                    )
                elif isinstance(poly_points, list):
                    s = 0.6
                    pts = [ft.Offset(p[0] * s + 10, p[1] * s + 10)
                           for p in poly_points]
                    cp.shapes.append(
                        cv.Path(
                            [cv.Path.MoveTo(pts[0].x, pts[0].y)]
                            + [cv.Path.LineTo(p.x, p.y) for p in pts[1:]]
                            + [cv.Path.Close()],
                            ft.Paint(color=color, style=ft.PaintingStyle.FILL),
                        )
                    )

                value_label = ft.Text(
                    "?", size=20, weight=ft.FontWeight.BOLD, color="white")
                d = ft.Container(
                    content=ft.Stack([cp, value_label]),
                    width=70, height=70,
                    scale=0,
                    top=random.randint(0, 50),
                    left=random.randint(40, 240),
                    animate_scale=ft.Animation(
                        400, ft.AnimationCurve.BOUNCE_OUT),
                    animate_position=ft.Animation(
                        400, ft.AnimationCurve.EASE_OUT),
                    animate_rotation=ft.Animation(
                        400, ft.AnimationCurve.EASE_OUT),
                )
                self.dice_area.controls.append(d)
                dice_to_animate.append((d, value_label, val, sides))

        self.update()
        await asyncio.sleep(0.1)

        for d, _label, _, _ in dice_to_animate:
            d.scale = 1.0
            d.top += 100
            d.rotate = random.uniform(-0.5, 0.5)
        self.update()

        for _ in range(12):
            for _d, label, _, sides in dice_to_animate:
                label.value = str(random.randint(1, sides))
            self.update()
            await asyncio.sleep(0.08)

        for d, label, val, _ in dice_to_animate:
            label.value = str(val)
            d.scale = 1.2
            d.rotate = 0
        self.update()

        self.result_overlay.visible = True
        self.total_text.value = str(final_total)

        self.update()
        await asyncio.sleep(0.5)
        self.result_overlay.opacity = 1

        if hasattr(self, "_haptic"):
            await self._haptic.heavy_impact()
        self.update()

    async def handle_exit(self, e):
        self.result_overlay.opacity = 0
        self.update()
        await asyncio.sleep(0.4)
        self.roll_btn.disabled = False
        self.bonus_input.disabled = False
        self.result_overlay.visible = False
        self.dice_rows_container.disabled = False

        self.dice_area.controls.clear()
        self.update()
        if self.on_close:
            result = self.on_close()
            if asyncio.iscoroutine(result):
                await result
