import os
import sys
import json
import queue
import atexit
import logging
from datetime import datetime, timezone
from src.config.env import get_env_bool
from logging.handlers import RotatingFileHandler, QueueHandler, QueueListener

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "ts":  datetime.now(timezone.utc).isoformat(),
            "lvl": record.levelname,
            "log": record.name,
            "msg": record.getMessage(),
            "mod": record.module,
            "fn":  record.funcName,
            "ln":  record.lineno,
        }
        if record.exc_info: log_record["exc"] = self.formatException(record.exc_info)
        return json.dumps(log_record, ensure_ascii=False)


def setup_logging(
    *,
    log_dir: str = "logs",
    app_name: str = "app",
    dev_mode: bool | None = None,        
    max_bytes: int = 1 * 1024 * 1024, 
    backup_count: int = 2,
) -> QueueListener:
    
    if dev_mode is None:
        dev_mode = get_env_bool("IS_DEV").unwrap_or(False)
        
    os.makedirs(log_dir, exist_ok=True)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG if dev_mode else logging.WARNING)

    formatter = JsonFormatter()
    handlers: list[logging.Handler] = []

    file_handler = RotatingFileHandler(
        os.path.join(log_dir, f"{app_name}.log"),
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG if dev_mode else logging.WARNING)
    file_handler.setFormatter(formatter)
    handlers.append(file_handler)

    error_handler = RotatingFileHandler(
        os.path.join(log_dir, f"{app_name}.error.log"),
        maxBytes=512 * 1024, 
        backupCount=1,
        encoding="utf-8",
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    handlers.append(error_handler)

    if dev_mode:
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter("%(levelname)-8s %(name)s — %(message)s"))
        handlers.append(console)

    log_queue: queue.Queue = queue.Queue(maxsize=1000)
    root.addHandler(QueueHandler(log_queue))

    listener = QueueListener(log_queue, *handlers, respect_handler_level=True)
    listener.start()

    atexit.register(listener.stop)

    return listener