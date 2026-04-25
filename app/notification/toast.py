from app.config.logger import Log, Level
from app.view.components.ui.toast import ToastLevel, ToastManager

class ToastNotifier:
    _LEVEL_MAP = {
        Level.INFO:    ToastLevel.INFO,
        Level.WARNING: ToastLevel.WARNING,
        Level.ERROR:   ToastLevel.ERROR,
    }

    def __init__(self, manager: ToastManager):
        self._manager = manager

    def on_log(self, log: Log) -> None:
        level = self._LEVEL_MAP.get(log.level)
        if level:
            self._manager.show(log.message, level)
