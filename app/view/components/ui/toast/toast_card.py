from __future__ import annotations

import time
import asyncio
import threading
import flet as ft
from typing import Callable
from app.view.style import settings
from app.view.components.ui.toast.toast import Toast
from app.view.components.common import Icon, Label, Title
from app.view.components.ui.toast.toast_classes import CLASSES


def ToastCard(
    toast: Toast,
    page: ft.Page,
    on_dismiss: Callable[[str], None],
    dismiss_event: threading.Event,
) -> ft.Container:
    theme = CLASSES[toast.level]
    duration = theme.duration

    icon = ft.Container(
        content=Icon(theme.icon, size=18, color=theme.border_color),
        bgcolor=ft.Colors.with_opacity(0.12, theme.border_color),
        padding=10,
        border_radius=12,
    )

    close = ft.Container(
        content=Icon(
            settings._main_icons["close"],
            size=14,
            color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
        ),
        padding=6,
        border_radius=8,
        on_click=lambda _, tid=toast.id: on_dismiss(tid),
        ink=True,
    )

    texts: list[ft.Control] = []
    if toast.title:
        texts.append(
            Title(
                value=toast.title,
                color=ft.Colors.WHITE,
                font_family="default",
                size=14,
                text_align=ft.TextAlign.LEFT,
            )
        )
    texts.append(
        Label(
            value=toast.message,
            color=ft.Colors.with_opacity(0.6, ft.Colors.WHITE),
            font_family="default",
            size=12,
            letter_spacing=0,
            text_align=ft.TextAlign.LEFT,
        )
    )

    progress_bar = ft.ProgressBar(
        value=1.0,
        bar_height=2,
        color=theme.border_color,
        bgcolor=ft.Colors.TRANSPARENT,
        border_radius=0,
        expand=True,
    )

    content = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        icon,
                        ft.Column(
                            controls=texts, spacing=2,
                            expand=True, tight=True
                        ),
                        close,
                    ],
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=ft.padding.only(left=16, top=12, right=10, bottom=14),
            ),
            ft.Container(
                width=3,
                left=0,
                top=0,
                bottom=0,
                bgcolor=theme.border_color,
            ),
            ft.Container(
                content=progress_bar,
                bottom=0,
                left=0,
                right=0,
                visible=duration is not None,
            ),
        ]
    )

    card = ft.Container(
        content=content,
        bgcolor=settings._main_colors["bg_dark"],
        border_radius=12,
        border=ft.border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=-5,
            color=ft.Colors.with_opacity(
                0.4, settings._main_colors["bg_dark"]),
            offset=ft.Offset(0, 8),
        ),
        offset=ft.Offset(0, -0.4),
        animate_offset=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
    )

    _drag_x = [0.0]

    def _on_update(e: ft.DragUpdateEvent) -> None:
        delta = getattr(e, "primary_delta", 0.0) or 0.0
        _drag_x[0] += delta
        card.offset = ft.Offset(_drag_x[0] / 100, 0)
        card.update()

    def _on_end(e: ft.DragEndEvent, tid: str = toast.id) -> None:
        velocity = getattr(e, "primary_velocity", 0.0) or 0.0
        distance = _drag_x[0]
        _drag_x[0] = 0.0

        if abs(velocity) > 400 or abs(distance) > 64:
            card.offset = ft.Offset(-1 if (distance <
                                    0 or velocity < 0) else 1, 0)
            card.update()
            time.sleep(0.15)
            on_dismiss(tid)
        else:
            card.offset = ft.Offset(0, 0)
            card.update()

    async def start_animations() -> None:
        await asyncio.sleep(0.05)
        if dismiss_event.is_set():
            return

        card.offset = ft.Offset(0, 0)
        page.update()

    page.run_task(start_animations)

    if duration is not None:
        async def animate_progress() -> None:
            start = time.perf_counter()

            while not dismiss_event.is_set():
                elapsed = time.perf_counter() - start
                remaining = max(0.0, 1.0 - (elapsed / float(duration)))

                if remaining <= 0:
                    break

                progress_bar.value = remaining
                page.update()
                await asyncio.sleep(0.05)

        page.run_task(animate_progress)

    return ft.Container(
        data=toast.id,
        animate=ft.Animation(220, ft.AnimationCurve.EASE_OUT),
        content=ft.GestureDetector(
            on_horizontal_drag_update=_on_update,
            on_horizontal_drag_end=_on_end,
            drag_interval=1,
            content=card,
        ),
    )
