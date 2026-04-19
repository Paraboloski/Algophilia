import random
from typing import List, Tuple
from src.view.components.common import Stack
from src.view.components import DiceCanvas

_DiceEntry = Tuple[DiceCanvas, int, int]
 
class DiceAnimationArea(Stack):
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
        if not rolls: return

        count = len(rolls)
        dice_size = 70
        if count > 12: dice_size = 55
        if count > 20: dice_size = 45
        if count > 35: dice_size = 35

        drop_y = 100
        margin = 10
        
        w = self.width if self.width is not None else 350
        h = self.height if self.height is not None else 250
        
        cols = int(max(1, (w - margin) // dice_size))
        rows = int(max(1, (h - drop_y - margin) // dice_size))
        
        positions = []
        for r in range(rows):
            for c in range(cols):
                x = c * dice_size + (w - cols * dice_size) / 2
                y = r * dice_size + 5 
                positions.append((x, y))
        
        random.shuffle(positions)

        for i, (val, sides) in enumerate(rolls):
            if i < len(positions):
                left, top = positions[i]
            else:
                left = random.uniform(0, w - dice_size)
                top = random.uniform(0, h - drop_y - dice_size)
            
            jitter = dice_size * 0.15
            left += random.uniform(-jitter, jitter)
            top += random.uniform(-jitter, jitter)
            
            left = max(2, min(left, w - dice_size - 2))
            top = max(2, min(top, h - drop_y - dice_size - 2))

            canvas = DiceCanvas(
                sides=sides,
                top=top,
                left=left,
                size=dice_size,
                scale=0.0,
            )
            self.controls.append(canvas)
            self._entries.append((canvas, val, sides))
 
    async def animate(self, update_fn) -> None:
        import asyncio
        for canvas, _, _ in self._entries:
            canvas.scale = 1.0
            canvas.top = (canvas.top or 0) + 100
            canvas.rotate = random.uniform(-0.3, 0.3)
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