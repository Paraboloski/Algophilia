from __future__ import annotations

import asyncio
import threading
import flet as ft
from app.events.logger import Logger
from app.models import Log, LogLevel
from app.view.components.ui.toast.toast import Toast
from app.view.components.ui.toast.toast_card import ToastCard
from app.view.components.ui.toast.toast_themes import Level, THEMES


MAX = 3

MAP_LOG_LEVEL_TO_TOAST_LEVEL: dict[LogLevel, Level] = {
    LogLevel.INFO:    Level.INFO,
    LogLevel.WARNING: Level.WARNING,
    LogLevel.ERROR:   Level.ERROR,
}


class ToastManager:
    def __init__(self, page: ft.Page, logger: Logger, safe_area_top: int, overlay_host: ft.Stack | None = None) -> None:
        self._page = page
        
        self._logger = logger

        self._is_closed = False

        self._active_toasts: list[Toast] = []

        self._queued_toasts: list[Toast] = []

        self._dismiss_events: dict[str, threading.Event] = {}

        self._lock = threading.RLock()

        self._toast_column = ft.Column(
            controls=[],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        )

        self._overlay_layer = ft.Container(
            content=self._toast_column,
            top=safe_area_top,
            left=12,
            right=12,
        )

        if overlay_host is None:
            self._page.overlay.append(self._overlay_layer)
        else:
            overlay_host.controls.append(self._overlay_layer)

        self._logger.subscribe(self.on_new_log)

    def info(self, message: str, title: str | None = None) -> None:
        self.show(message, Level.INFO, title)

    def warning(self, message: str, title: str | None = None) -> None:
        self.show(message, Level.WARNING, title)

    def error(self, message: str, title: str | None = None) -> None:
        self.show(message, Level.ERROR, title)

    def show(self, message: str, level: Level, title: str | None = None) -> None:
        new_toast = Toast._(message, level, title)

        with self._lock:
            if self._is_closed:
                return

            if len(self._active_toasts) >= MAX:
                self._queued_toasts.append(new_toast)
                return
        self.toast(new_toast)

    def close(self) -> None:
        with self._lock:
            if self._is_closed:
                return

            self._is_closed = True

            self._logger.unsubscribe(self.on_new_log)

            for dismiss_event in self._dismiss_events.values():
                dismiss_event.set()

            self._dismiss_events.clear()
            self._active_toasts.clear()
            self._queued_toasts.clear()
            self._toast_column.controls.clear()

    def on_new_log(self, log: Log) -> None:
        if not self._is_closed:
            self._page.run_task(self.show_from_log, log)

    async def show_from_log(self, log: Log) -> None:
        toast_level = MAP_LOG_LEVEL_TO_TOAST_LEVEL.get(log.level)
        if toast_level is None:
            return

        if log.exception:
            message = f"{log.message} | {log.exception}"
        else:
            message = log.message

        self.show(message=message, level=toast_level, title=log.origin)

    def toast(self, toast: Toast) -> None:
        theme = THEMES[toast.level]

        dismiss_event = threading.Event()

        with self._lock:
            if self._is_closed:
                return
            self._active_toasts.append(toast)
            self._dismiss_events[toast.id] = dismiss_event

        toast_card = ToastCard(
            toast=toast,
            page=self._page,
            on_dismiss=self.dismiss,
            dismiss_event=dismiss_event,
        )
        self._toast_column.controls.append(toast_card)
        self._page.update()

        if theme.duration is not None:
            self._page.run_task(
                self.wait,
                toast.id,
                float(theme.duration),
                dismiss_event,
            )

    async def wait(
        self,
        toast_id: str,
        duration: float,
        dismiss_event: threading.Event,
    ) -> None:

        await asyncio.sleep(duration)

        if not dismiss_event.is_set():
            self.dismiss(toast_id)

    def dismiss(self, toast_id: str) -> None:
        next_toast: Toast | None = None

        with self._lock:
            if self._is_closed:
                return
            if not self.is_active(toast_id):
                return

            self.remove(toast_id)
            if self._queued_toasts:
                next_toast = self._queued_toasts.pop(0)

        self._page.update()

        if next_toast is not None:
            self.toast(next_toast)

    def is_active(self, toast_id: str) -> bool:
        for toast in self._active_toasts:
            if toast.id == toast_id:
                return True
        return False

    def remove(self, toast_id: str) -> None:
        dismiss_event = self._dismiss_events.pop(toast_id, None)
        if dismiss_event is not None:
            dismiss_event.set()
        self._active_toasts = [
            t for t in self._active_toasts if t.id != toast_id
        ]

        self._toast_column.controls = [
            control for control in self._toast_column.controls
            if getattr(control, "data", None) != toast_id
        ]
