import shutil
from pathlib import Path


class Directory:
    def __init__(self, directory: str):
        self._directory = Path(directory)
        self.mkdir()

    def mkdir(self) -> None:
        self._directory.mkdir(parents=True, exist_ok=True)

    def rmdir(self) -> None:
        if self._directory.exists():
            shutil.rmtree(self._directory)

    def write(self, filename: str, content: str) -> None:
        path = self._directory / filename
        file = path.open("a", encoding="utf-8")
        try:
            file.write(f"{content}\n")
        finally:
            file.close()
