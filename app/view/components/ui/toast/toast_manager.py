from __future__ import annotations

import asyncio
import threading
import flet as ft
from app.events.logger import Logger
from app.models import Log, LogLevel
from app.view.components.ui.toast.toast import Toast
from app.view.components.ui.toast.toast_card import ToastCard
from app.view.components.ui.toast.toast_classes import Level, CLASSES

_MAX = 3

_MAP: dict[LogLevel, Level] = {
    LogLevel.INFO:    Level.INFO,
    LogLevel.WARNING: Level.WARNING,
    LogLevel.ERROR:   Level.ERROR,
}


class ToastManager:
    def __init__(
        self,
        page: ft.Page,
        logger: Logger,
        safe_area_top: int,
        overlay_host: ft.Stack | None = None,
    ) -> None:
        self._page = page
        self._closed = False
        self._logger = logger

        self._active: list[Toast] = []
        self._queue:  list[Toast] = []
        self._dismiss_events: dict[str, threading.Event] = {}
        self._lock = threading.RLock()

        self._col = ft.Column(
            controls=[],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        )
        self._layer = ft.Container(
            content=self._col,
            top=safe_area_top,
            left=12,
            right=12,
        )

        host = page.overlay if overlay_host is None else overlay_host.controls
        host.append(self._layer)

        self._logger.subscribe(self._get_log)

    def info(self, message: str, title: str | None = None) -> None:
        self.show(message, Level.INFO, title)

    def warning(self, message: str, title: str | None = None) -> None:
        self.show(message, Level.WARNING, title)

    def error(self, message: str, title: str | None = None) -> None:
        self.show(message, Level.ERROR, title)

    def show(self, message: str, level: Level, title: str | None = None) -> None:
        toast = Toast.make(message, level, title)

        with self._lock:
            if self._closed:
                return
            if len(self._active) >= _MAX:
                self._queue.append(toast)
                return

        self._build(toast)

    def close(self) -> None:
        with self._lock:
            if self._closed:
                return

            self._closed = True
            self._logger.unsubscribe(self._get_log)

            for event in self._dismiss_events.values():
                event.set()

            self._dismiss_events.clear()
            self._active.clear()
            self._queue.clear()
            self._col.controls.clear()

    def _get_log(self, log: Log) -> None:
        if not self._closed:
            self._page.run_task(self._show, log)

    async def _show(self, log: Log) -> None:
        level = _MAP.get(log.level)
        if level is None:
            return

        message = f"{log.message} | {log.exception}" if log.exception else log.message
        self.show(message=message, level=level, title=log.origin)

    def _build(self, toast: Toast) -> None:
        theme = CLASSES[toast.level]
        dismiss_event = threading.Event()

        with self._lock:
            if self._closed:
                return
            self._active.append(toast)
            self._dismiss_events[toast.id] = dismiss_event

        self._col.controls.append(ToastCard(
            toast=toast,
            page=self._page,
            on_dismiss=self._dismiss,
            dismiss_event=dismiss_event,
        ))
        self._page.update()

        if theme.duration is not None:
            self._page.run_task(
                self._get_dismiss, toast.id, float(
                    theme.duration), dismiss_event
            )

    async def _get_dismiss(
        self,
        toast_id: str,
        duration: float,
        dismiss_event: threading.Event,
    ) -> None:
        await asyncio.sleep(duration)
        if not dismiss_event.is_set():
            self._dismiss(toast_id)

    def _dismiss(self, toast_id: str) -> None:
        next_toast: Toast | None = None

        with self._lock:
            if self._closed or not self._is_active(toast_id):
                return

            self._remove(toast_id)
            next_toast = self._queue.pop(0) if self._queue else None

        self._page.update()

        if next_toast:
            self._build(next_toast)

    def _is_active(self, toast_id: str) -> bool:
        return any(t.id == toast_id for t in self._active)

    def _remove(self, toast_id: str) -> None:
        event = self._dismiss_events.pop(toast_id, None)
        if event:
            event.set()

        self._active = [t for t in self._active if t.id != toast_id]
        self._col.controls = [
            control for control in self._col.controls
            if getattr(control, "data", None) != toast_id
        ]
