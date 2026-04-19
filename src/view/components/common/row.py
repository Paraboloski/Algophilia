import flet as ft
from typing import Optional, List, Union

class Row(ft.Row):
    def __init__(
        self,
        controls: Optional[List[ft.Control]] = None,
        alignment: Optional[ft.MainAxisAlignment] = None,
        vertical_alignment: Optional[ft.CrossAxisAlignment] = None,
        spacing: Optional[Union[int, float]] = None,
        wrap: bool = False,
        **kwargs
    ):
        init_kwargs = {k: v for k, v in {
            "controls": controls,
            "alignment": alignment,
            "vertical_alignment": vertical_alignment,
            "spacing": spacing,
            "wrap": wrap,
        }.items() if v is not None}
        
        init_kwargs.update(kwargs)
        super().__init__(**init_kwargs)
