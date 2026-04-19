import flet as ft
from typing import Optional, List, Callable

class Dropdown(ft.Dropdown):
    def __init__(
        self,
        options: Optional[List[ft.DropdownOption]] = None,
        value: Optional[str] = None,
        label: Optional[str] = None,
        width: Optional[int] = None,
        on_change: Optional[Callable] = None,
        **kwargs
    ):
        init_kwargs = {k: v for k, v in {
            "options": options,
            "value": value,
            "label": label,
            "width": width,
            "on_change": on_change,
        }.items() if v is not None}
        
        init_kwargs.update(kwargs)
        super().__init__(**init_kwargs)
