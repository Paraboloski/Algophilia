from pathlib import Path

class Error(Exception):
    pass

class MissingVariable(Error):
    def __init__(self, key: str):
        super().__init__(f"Variabile mancante: '{key}'")
        self.key = key


class InvalidValue(Error):
    def __init__(self, key: str, value: str):
        super().__init__(f"Valore non valido per '{key}': '{value}'")
        self.key = key
        self.value = value


class CastError(Error):
    def __init__(self, key: str, value: str, target: str):
        super().__init__(f"Impossibile convertire '{key}={value!r}' in {target}")
        self.key = key
        self.value = value
        self.target = target
        

class ConnectionError(Error):
    def __init__(self, reason: str):
        super().__init__(f"Errore di connessione: {reason}")
        self.reason = reason

class SchemaNotFound(Error):
    def __init__(self, path: Path):
        super().__init__(f"Schema non trovato: '{path}'")
        self.path = path

class ExecutionError(Error):
    def __init__(self, sql: str, cause: Exception):
        super().__init__(f"Errore eseguendo query: {cause}")
        self.sql = sql
        self.cause = cause