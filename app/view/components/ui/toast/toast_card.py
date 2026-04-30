from __future__ import annotations

import time
import asyncio
import threading
import flet as ft
from typing import Callable
from app.view.style import settings
from app.view.components.ui.toast.toast import Toast
from app.view.components.common import Icon, Label, Title
from app.view.components.ui.toast.toast_themes import THEMES


SWIPE_SPEED = 400.0
SWIPE_DISTANCE = 65.0
SWIPE_DURATION = 0.15
START_ANIMATION = 0.05
UPDATE_INTERVAL = 0.01


def card_content(title: str | None, message: str) -> ft.Column:
    controls_list: list[ft.Control] = []

    if title is not None:
        controls_list.append(Title(
            value=title,
            color=ft.Colors.WHITE,
            font_family="default",
            size=14,
            text_align=ft.TextAlign.LEFT,
        ))

    controls_list.append(Label(
        value=message,
        color=ft.Colors.with_opacity(0.6, ft.Colors.WHITE),
        font_family="default",
        size=12,
        letter_spacing=0,
        text_align=ft.TextAlign.LEFT,
    ))

    return ft.Column(
        controls=controls_list,
        spacing=2,
        expand=True,
        tight=True,
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

        self._page = page
        self._toast = toast
        self._on_dismiss = on_dismiss
        self._dismiss_event = dismiss_event
        self.data = toast.id

        self._theme = THEMES[toast.level]

        self._horizontal_drag = 0.0
        self._card = self._build()

        self.animate = ft.Animation(220, ft.AnimationCurve.EASE_OUT)
        self.content = ft.GestureDetector(
            on_horizontal_drag_update=self._on_drag_update,
            on_horizontal_drag_end=self._on_drag_end,
            drag_interval=1,
            content=self._card,
        )

        self._start_animate()

        if self._theme.duration is not None:
            self._start_progress_animation()

    def _build(self) -> ft.Container:
        theme = self._theme

        self._progress_bar = ft.ProgressBar(
            value=1.0,
            bar_height=2,
            color=theme.border_color,
            bgcolor=ft.Colors.TRANSPARENT,
            border_radius=0,
            expand=True,
        )

        self._close_button = ft.Container(
            content=Icon(
                settings._main_icons["close"],
                size=14,
            ),
            padding=6,
            border_radius=8,
            bgcolor=ft.Colors.TRANSPARENT,
            animate=ft.Animation(140, ft.AnimationCurve.EASE_OUT),
            on_click=lambda e: self._on_dismiss(self._toast.id),
            ink=True,
        )

        row: list[ft.Control] = [
            ft.Container(
                content=Icon(
                    theme.icon,
                    size=18,
                    color=theme.border_color,
                ),
                bgcolor=ft.Colors.with_opacity(0.12, theme.border_color),
                padding=10,
                border_radius=12,
            ),
            card_content(self._toast.title, self._toast.message),
            self._close_button,
        ]

        stack: list[ft.Control] = [
            ft.Container(
                content=ft.Row(
                    controls=row,
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
                content=self._progress_bar,
                bottom=0,
                left=0,
                right=0,
                visible=theme.duration is not None,
            ),
        ]

        card = ft.Container(
            content=ft.Stack(controls=stack),
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

        return card

    def _on_drag_update(self, event: ft.DragUpdateEvent) -> None:
        delta = getattr(event, "primary_delta", 0.0) or 0.0

        self._horizontal_drag += delta

        self._card.offset = ft.Offset(self._horizontal_drag / 100, 0)
        self._card.update()

    def _on_drag_end(self, event: ft.DragEndEvent) -> None:
        velocity = getattr(event, "primary_velocity", 0.0) or 0.0
        _distance = self._horizontal_drag

        self._horizontal_drag = 0.0

        is_close = self._dismiss_on_swipe(velocity, _distance)

        if is_close:
            if _distance < 0 or velocity < 0:
                exit_direction = -1  # sinistra
            else:
                exit_direction = 1   # destra

            self._card.offset = ft.Offset(exit_direction, 0)
            self._card.update()

            time.sleep(SWIPE_DURATION)

            self._on_dismiss(self._toast.id)
        else:
            self._card.offset = ft.Offset(0, 0)
            self._card.update()

    def _dismiss_on_swipe(self, velocity: float, distance: float) -> bool:
        velocity_is_high = abs(velocity) > SWIPE_SPEED
        distance_is_far = abs(distance) > SWIPE_DISTANCE

        return velocity_is_high or distance_is_far

    def _start_animate(self) -> None:
        self._page.run_task(self._run_toast_animation)

    def _start_progress_animation(self) -> None:
        self._page.run_task(self._run_bar_animation)

    async def _run_toast_animation(self) -> None:
        await asyncio.sleep(START_ANIMATION)

        if not self._dismiss_event.is_set():
            self._card.offset = ft.Offset(0, 0)
            self._page.update()

    async def _run_bar_animation(self) -> None:
        if self._theme.duration is None:
            return

        duration = float(self._theme.duration)
        start = time.time()

        while not self._dismiss_event.is_set():
            end = 1.0 - (time.time() - start) / duration

            if end < 0.0:
                end = 0.0

            self._progress_bar.value = end
            self._page.update()

            if end <= 0.0:
                self._on_dismiss(self._toast.id)
                break

            await asyncio.sleep(UPDATE_INTERVAL)
