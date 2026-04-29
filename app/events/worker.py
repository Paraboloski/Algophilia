import threading
from queue import Queue
from app.models import Log
from typing import Any, Callable, Optional


class Worker:
    def __init__(self):
        self._is_shutdown = False
        self._shutdown_lock = threading.Lock()
        self._subscribers_lock = threading.Lock()
        self._queue: Queue[Optional[Log]] = Queue()
        self._subscribers: list[Callable[[Log], None]] = []

        self._thread = threading.Thread(
            target=self._process_queue, daemon=True)
        self._thread.start()

    def subscribe(self, callback: Callable[[Log], Any]):
        with self._subscribers_lock:
            self._subscribers.append(callback)

    def unsubscribe(self, callback: Callable[[Log], Any]):
        with self._subscribers_lock:
            self._subscribers = [
                sub for sub in self._subscribers if sub != callback]

    def dispatch(self, log: Log):
        if self._is_shutdown:
            return
        self._queue.put(log)

    def _process_queue(self):
        while True:
            log = self._queue.get()

            if log is None:
                self._queue.task_done()
                break

            with self._subscribers_lock:
                subscribers = list(self._subscribers)

            for sub in subscribers:
                threading.Thread(target=sub, args=(log,), daemon=True).start()

            self._queue.task_done()

    def shutdown(self):
        with self._shutdown_lock:
            if self._is_shutdown:
                return
            self._is_shutdown = True
            self._queue.put(None)

        self._queue.join()
        self._thread.join(timeout=1)
