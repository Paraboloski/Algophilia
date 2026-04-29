from __future__ import annotations

import asyncio
import threading
import flet as ft
from typing import Optional
from app.events.logger import Logger
from app.models import Log, LogLevel
from app.view.components.ui.toast.toast import Toast
from app.view.components.ui.toast.toast_card import ToastCard
from app.view.components.ui.toast.toast_classes import Level, CLASSES


class ToastManager:
    def __init__(
        self,
        page: ft.Page,
        logger: Logger,
        safe_area_top: int,
        overlay_host: Optional[ft.Stack] = None,
    ) -> None:
        self._page = page
        self._logger = logger
        self._closed = False
        self._active: list[Toast] = []
        self._queue: list[Toast] = []
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

        if overlay_host is None:
            page.overlay.append(self._layer)
        else:
            overlay_host.controls.append(self._layer)

        self._logger.subscribe(self._on_log)

    def info(self, message: str, title: Optional[str] = None) -> None:
        self.show(message, Level.INFO, title)

    def warning(self, message: str, title: Optional[str] = None) -> None:
        self.show(message, Level.WARNING, title)

    def error(self, message: str, title: Optional[str] = None) -> None:
        self.show(message, Level.ERROR, title)

    def show(self, message: str, level: Level, title: Optional[str] = None) -> None:
        toast = Toast.make(message, level, title)
        with self._lock:
            if self._closed:
                return
            if len(self._active) < 3:
                mount_now = True
            else:
                mount_now = False
                self._queue.append(toast)

        if mount_now:
            self._mount(toast)

    def _on_log(self, log: Log) -> None:
        if self._closed:
            return
        self._page.run_task(self._show_from_log, log)

    async def _show_from_log(self, log: Log) -> None:
        level = self._map_log_level(log.level)
        if level is None:
            return

        message = log.message
        if log.exception:
            message = f"{message} | {log.exception}"

        self.show(message=message, level=level, title=log.origin)

    def _map_log_level(self, log_level: LogLevel) -> Optional[Level]:
        if log_level == LogLevel.INFO:
            return Level.INFO
        if log_level == LogLevel.WARNING:
            return Level.WARNING
        if log_level == LogLevel.ERROR:
            return Level.ERROR
        return None

    def _mount(self, toast: Toast) -> None:
        with self._lock:
            if self._closed:
                return
            self._active.append(toast)
            theme = CLASSES[toast.level]
            dismiss_event = threading.Event()
            self._dismiss_events[toast.id] = dismiss_event

        self._col.controls.append(
            ToastCard(
                toast=toast,
                page=self._page,
                on_dismiss=self._dismiss,
                dismiss_event=dismiss_event,
            )
        )
        self._page.update()

        if theme.duration is not None:
            self._page.run_task(self._auto_dismiss, toast.id,
                                float(theme.duration), dismiss_event)

    async def _auto_dismiss(
        self,
        toast_id: str,
        duration: float,
        dismiss_event: threading.Event,
    ) -> None:
        await asyncio.sleep(duration)

        if dismiss_event.is_set():
            return

        self._dismiss(toast_id)

    def _dismiss(self, toast_id: str) -> None:
        with self._lock:
            if self._closed:
                return
            if not any(t.id == toast_id for t in self._active):
                return

            dismiss_event = self._dismiss_events.pop(toast_id, None)
            if dismiss_event:
                dismiss_event.set()

            self._active = [t for t in self._active if t.id != toast_id]
            self._col.controls = [
                c for c in self._col.controls
                if getattr(c, "data", None) != toast_id
            ]
            next_toast = self._queue.pop(0) if self._queue else None

        if next_toast:
            self._mount(next_toast)

        self._page.update()

    def close(self) -> None:
        with self._lock:
            if self._closed:
                return

            self._closed = True
            self._logger.unsubscribe(self._on_log)

            for dismiss_event in self._dismiss_events.values():
                dismiss_event.set()
            self._dismiss_events.clear()
            self._active.clear()
            self._queue.clear()
            self._col.controls.clear()
