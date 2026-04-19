import flet as ft
import flet.canvas as cv
from typing import List, cast
from src.view.components.common import Container, Stack

class DiceCanvas(Container):
    POLYGONS: dict = {
        4:   [[50, 10], [90, 85], [10, 85]],
        6:   [[15, 15], [85, 15], [85, 85], [15, 85]],
        8:   [[50, 5],  [90, 50], [50, 95], [10, 50]],
        10:  [[50, 5],  [90, 40], [50, 95], [10, 40]],
        12:  [[50, 5],  [90, 35], [75, 90], [25, 90], [10, 35]],
        20:  [[50, 5],  [90, 25], [90, 75], [50, 95], [10, 75], [10, 25]],
        100: "circle",
    }

    DICE_COLORS: dict = {
        4:   "#4CAF50",
        6:   "#2196F3",
        8:   "#9C27B0",
        10:  "#E91E63",
        12:  "#F44336",
        20:  "#FF9800",
        100: "#795548",
    }

    def __init__(
        self,
        sides: int,
        top: int | float = 0,
        left: int | float = 0,
        size: int = 70,
        scale: float = 0.0,
        rotate: float = 0.0,
        color: str | None = None,
    ):
        self._value_label = ft.Text(
            "?",
            size=int(size * 0.3),  
            weight=ft.FontWeight.BOLD,
            color="white",
            text_align=ft.TextAlign.CENTER,
            no_wrap=True,
        )

        canvas = self._build_canvas(
            sides=sides,
            color=color or self.DICE_COLORS.get(sides, "#FFD700"),
            size=size,
        )

        label_wrapper = Container(
            content=self._value_label,
            width=size,
            height=size,
            top=0,
            left=0,
            alignment=ft.Alignment(0, 0),
        )

        super().__init__(
            content=Stack(
                controls=cast(List[ft.Control], [canvas, label_wrapper]),
                width=size,
                height=size,
            ),
            width=size,
            height=size,
            scale=scale,
            top=top,
            left=left,
            rotate=rotate,
            animate_scale=ft.Animation(400, ft.AnimationCurve.BOUNCE_OUT),
            animate_position=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            animate_rotation=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
        )

    def set_value(self, value: int | str) -> None: self._value_label.value = str(value)

    @property
    def value_label(self) -> ft.Text: return self._value_label

    @staticmethod
    def _build_canvas(sides: int, color: str, size: int) -> cv.Canvas:
        cp = cv.Canvas(width=size, height=size)
        poly = DiceCanvas.POLYGONS.get(sides)

        if poly == "circle":
            r = size / 2
            cp.shapes.append(cv.Circle(r, r, r - 5, ft.Paint(color=color, style=ft.PaintingStyle.FILL)))
        elif isinstance(poly, list):
            scale = size / 100 * 0.7
            offset = size * 0.15
            pts = [ft.Offset(p[0] * scale + offset, p[1] * scale + offset) for p in poly]
            cp.shapes.append(
                cv.Path(
                    [cv.Path.MoveTo(pts[0].x, pts[0].y)]
                    + [cv.Path.LineTo(p.x, p.y) for p in pts[1:]]
                    + [cv.Path.Close()],
                    ft.Paint(color=color, style=ft.PaintingStyle.FILL),
                )
            )
        return cp