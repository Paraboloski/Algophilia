import flet as ft
from pathlib import Path


def Image(path: Path, fit: ft.BoxFit, opacity: float = 1.0) -> ft.DecorationImage:
    return ft.DecorationImage(
        src=str(path),
        fit=fit,
        opacity=opacity,
    )
