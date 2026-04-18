import flet as ft
from typing import Optional, Union

class Container(ft.Container):
    def __init__(
        self,
        content: Optional[ft.Control] = None,
        width: Optional[Union[int, float]] = None,
        height: Optional[Union[int, float]] = None,
        padding: Optional[ft.PaddingValue] = None,
        margin: Optional[ft.MarginValue] = None,
        alignment: Optional[ft.Alignment] = None,
        bgcolor: Optional[str] = None,
        border_radius: Optional[ft.BorderRadiusValue] = None,
        **kwargs
    ):
        init_kwargs = {k: v for k, v in {
            "content": content,
            "width": width,
            "height": height,
            "padding": padding,
            "margin": margin,
            "alignment": alignment,
            "bgcolor": bgcolor,
            "border_radius": border_radius,
        }.items() if v is not None}
        
        init_kwargs.update(kwargs)
        super().__init__(**init_kwargs)
