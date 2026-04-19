import flet as ft
from typing import Optional, List, Union

class Column(ft.Column):
    def __init__(
        self,
        controls: Optional[List[ft.Control]] = None,
        alignment: Optional[ft.MainAxisAlignment] = None,
        horizontal_alignment: Optional[ft.CrossAxisAlignment] = None,
        spacing: Optional[Union[int, float]] = None,
        wrap: bool = False,
        **kwargs
    ):
        init_kwargs = {k: v for k, v in {
            "controls": controls,
            "alignment": alignment,
            "horizontal_alignment": horizontal_alignment,
            "spacing": spacing,
            "wrap": wrap,
        }.items() if v is not None}
        
        init_kwargs.update(kwargs)
        super().__init__(**init_kwargs)
