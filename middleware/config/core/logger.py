import os
import json
import queue
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler, QueueHandler, QueueListener


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if record.exc_info: log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record)


def setup_logging():
    if not os.path.exists("logs"): os.makedirs("logs")

    log_queue = queue.Queue(-1)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = JsonFormatter()

    info_handler = RotatingFileHandler(
        "logs/info.log",
        maxBytes=2 * 1024 * 1024,
        backupCount=5
    )
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    error_handler = RotatingFileHandler(
        "logs/error.log",
        maxBytes=2 * 1024 * 1024,
        backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    queue_handler = QueueHandler(log_queue)
    logger.addHandler(queue_handler)

    listener = QueueListener(
        log_queue,
        info_handler,
        error_handler,
        respect_handler_level=True
    )

    listener.start()

    return listener 