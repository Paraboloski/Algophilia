import flet as ft
from typing import Optional, List, Union

class Stack(ft.Stack):
    def __init__(
        self,
        controls: Optional[List[ft.Control]] = None,
        width: Optional[Union[int, float]] = None,
        height: Optional[Union[int, float]] = None,
        **kwargs
    ):
        init_kwargs = {k: v for k, v in {
            "controls": controls,
            "width": width,
            "height": height,
        }.items() if v is not None}
        
        init_kwargs.update(kwargs)
        super().__init__(**init_kwargs)
