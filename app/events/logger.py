import os
import inspect
from app.utils import Directory
from app.models import Log, LogLevel
from app.events.worker import Worker
from typing import Any, Callable, Optional


class Logger:
    def __init__(self, directory: Directory, worker: Worker):
        self._worker = worker
        self._directory = directory
        self._worker.subscribe(self.write)

    def write(self, log: Log)  -> None:
        self._directory.write(f"{log.level.value}.log", str(log))

    def get_origin(self) -> tuple[str, int]:
        info = inspect.stack()[3]
        return os.path.basename(info.filename), info.lineno

    def log(self, level: LogLevel, message: str, error: Optional[Any] = None)  -> None:
        origin, line = self.get_origin()

        log = Log(
            level=level,
            message=message,
            line=line,
            origin=origin,
            exception=str(error) if error else None,
        )

        self._worker.dispatch(log)

    def info(self, message: str) -> None: 
        self.log(LogLevel.INFO, message)

    def debug(self, message: str) -> None:
        self.log(LogLevel.DEBUG, message)

    def warn(self, message: str) -> None:
        self.log(LogLevel.WARNING, message)

    def error(self, message: str, err: Optional[Any] = None) -> None:
        self.log(LogLevel.ERROR, message, err)

    def subscribe(self, f: Callable[[Log], Any]) -> None:
        self._worker.subscribe(f)

    def unsubscribe(self, f: Callable[[Log], Any]) -> None:
        self._worker.unsubscribe(f)
