import random
import flet as ft
from typing import List, Tuple
from Frontend.src.components.ui import DiceCanvas

_DiceEntry = Tuple[DiceCanvas, int, int]
 
class DiceAnimationArea(ft.Stack):
    def __init__(
        self,
        width: int = 350,
        height: int = 250,
        shuffle_frames: int = 12,
        shuffle_delay: float = 0.08,
    ):
        super().__init__(width=width, height=height)
        self._shuffle_frames = shuffle_frames
        self._shuffle_delay = shuffle_delay
        self._entries: List[_DiceEntry] = []
 
    def clear(self) -> None:
        self.controls.clear()
        self._entries.clear()
 
    def populate(self, rolls: List[Tuple[int, int]]) -> None:
        self.clear()
        for val, sides in rolls:
            canvas = DiceCanvas(
                sides=sides,
                top=random.randint(0, 50),
                left=random.randint(40, 240),
                scale=0.0,
            )
            self.controls.append(canvas)
            self._entries.append((canvas, val, sides))
 
    async def animate(self, update_fn) -> None:
        import asyncio
        for canvas, _, _ in self._entries:
            canvas.scale = 1.0
            canvas.top = (canvas.top or 0) + 100
            canvas.rotate = random.uniform(-0.5, 0.5)
        update_fn()
        
        for _ in range(self._shuffle_frames):
            for canvas, _, sides in self._entries:
                canvas.set_value(random.randint(1, sides))
            update_fn()
            await asyncio.sleep(self._shuffle_delay)
            
        for canvas, val, _ in self._entries:
            canvas.set_value(val)
            canvas.scale = 1.2
            canvas.rotate = 0
        update_fn()