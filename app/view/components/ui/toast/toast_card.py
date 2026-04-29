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

_DELAY = 0.05
_INTERVAL = 0.05
_DURATION = 0.15
_SWIPE_SPEED = 400.0
_SWIPE_DISTANCE = 64.0


def _icon_badge(theme) -> ft.Container:
    return ft.Container(
        content=Icon(theme.icon, size=18, color=theme.border_color),
        bgcolor=ft.Colors.with_opacity(0.12, theme.border_color),
        padding=10,
        border_radius=12,
    )


def _close_button(on_click: Callable) -> ft.Container:
    return ft.Container(
        content=Icon(
            settings._main_icons["close"],
            size=14,
            color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
        ),
        padding=6,
        border_radius=8,
        on_click=on_click,
        ink=True,
    )


def _text_column(title: str | None, message: str) -> ft.Column:
    controls: list[ft.Control] = []

    if title:
        controls.append(Title(
            value=title,
            color=ft.Colors.WHITE,
            font_family="default",
            size=14,
            text_align=ft.TextAlign.LEFT,
        ))

    controls.append(Label(
        value=message,
        color=ft.Colors.with_opacity(0.6, ft.Colors.WHITE),
        font_family="default",
        size=12,
        letter_spacing=0,
        text_align=ft.TextAlign.LEFT,
    ))

    return ft.Column(controls=controls, spacing=2, expand=True, tight=True)


def _progress_bar(color, visible: bool) -> ft.ProgressBar:
    return ft.ProgressBar(
        value=1.0,
        bar_height=2,
        color=color,
        bgcolor=ft.Colors.TRANSPARENT,
        border_radius=0,
        expand=True,
    )


class ToastCard(ft.Container):
    def __init__(
        self,
        toast: Toast,
        page: ft.Page,
        on_dismiss: Callable[[str], None],
        dismiss_event: threading.Event,
    ) -> None:
        super().__init__()

        self._drag = 0.0
        self._page = page
        self._toast = toast
        self.data = toast.id
        self._on_dismiss = on_dismiss
        self._theme = CLASSES[toast.level]
        self._dismiss_event = dismiss_event

        self._card = self._build()

        self.animate = ft.Animation(220, ft.AnimationCurve.EASE_OUT)
        self.content = ft.GestureDetector(
            on_horizontal_drag_update=self._on_drag_start,
            on_horizontal_drag_end=self._on_drag_end,
            drag_interval=1,
            content=self._card,
        )

        self._start()

        if self._theme.duration is not None:
            self._progress_animation()

    def _build(self) -> ft.Container:
        theme = self._theme

        self._progress_bar = _progress_bar(
            color=theme.border_color,
            visible=theme.duration is not None,
        )

        body = ft.Stack(controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        _icon_badge(theme),
                        _text_column(
                            self._toast.title, self._toast.message),
                        _close_button(self._on_click_close),
                    ],
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=ft.padding.only(left=16, top=12, right=10, bottom=14),
            ),
            ft.Container(
                width=3,
                left=0, top=0, bottom=0,
                bgcolor=theme.border_color,
            ),
            ft.Container(
                content=self._progress_bar,
                bottom=0, left=0, right=0,
                visible=theme.duration is not None,
            ),
        ])

        return ft.Container(
            content=body,
            bgcolor=settings._main_colors["bg_dark"],
            border_radius=12,
            border=ft.border.all(
                1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
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

    def _on_click_close(self, _: ft.ControlEvent) -> None:
        self._on_dismiss(self._toast.id)

    def _on_drag_start(self, e: ft.DragUpdateEvent) -> None:
        self._drag += getattr(e, "primary_delta", 0.0) or 0.0
        self._card.offset = ft.Offset(self._drag / 100, 0)
        self._card.update()

    def _on_drag_end(self, e: ft.DragEndEvent) -> None:
        velocity = getattr(e, "primary_velocity", 0.0) or 0.0
        distance, self._drag = self._drag, 0.0

        if self._dismiss(velocity, distance):
            direction = -1 if (distance < 0 or velocity < 0) else 1
            self._card.offset = ft.Offset(direction, 0)
            self._card.update()
            time.sleep(_DURATION)
            self._on_dismiss(self._toast.id)
        else:
            self._card.offset = ft.Offset(0, 0)
            self._card.update()

    @staticmethod
    def _dismiss(velocity: float, distance: float) -> bool:
        return (
            abs(velocity) > _SWIPE_SPEED
            or abs(distance) > _SWIPE_DISTANCE
        )

    def _start(self) -> None:
        self._page.run_task(self._animation)

    def _progress_animation(self) -> None:
        self._page.run_task(self._animate_progress)

    async def _animation(self) -> None:
        await asyncio.sleep(_DELAY)
        if not self._dismiss_event.is_set():
            self._card.offset = ft.Offset(0, 0)
            self._page.update()

    async def _animate_progress(self) -> None:
        if self._theme.duration is None:
            return

        duration = float(self._theme.duration)
        start = time.perf_counter()

        while not self._dismiss_event.is_set():
            elapsed = time.perf_counter() - start
            remaining = max(0.0, 1.0 - elapsed / duration)

            self._progress_bar.value = remaining
            self._page.update()

            if remaining <= 0:
                break

            await asyncio.sleep(_INTERVAL)
