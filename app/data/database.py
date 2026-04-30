from pathlib import Path
from result import Result, Err, Ok
from app.data.seeder import Seeder
from app.events.logger import Logger
from aiosqlite import Connection, connect, Error
from app.utils.exception import AppError, ConnectionError, QueryError


class Database:
    def __init__(self, url: str, schema_path: str | None, seed_paths: list[Path], logger: Logger) -> None:
        self._logger = logger
        
        self._schema_path = schema_path
        
        self._database_url = url
        
        self._seed_paths = seed_paths
        
        self._connection: Connection | None = None

    def get_connection(self) -> Result[Connection, ConnectionError]:
        if not self._connection:
            exception = ConnectionError(
                url=self._database_url,
                action="get connection",
                details="Connessione non inizializzata. Richiesto start()."
            )
            self._logger.error(str(exception))
            return Err(exception)

        return Ok(self._connection)

    async def connect(self) -> Result[bool, AppError]:
        conn: Connection | None = None

        try:
            conn = await connect(self._database_url)
            self._logger.debug(f"Database: Connesso a {self._database_url}")

            if self._schema_path:
                script = Path(self._schema_path).read_text(encoding="utf-8")
                await conn.executescript(script)
                self._logger.debug(f"Database: Schema {Path(self._schema_path).name} applicato")

            tables: dict[str, Path] = {}

            for path in self._seed_paths:
                if path.exists():
                    tables[path.stem] = path
                else:
                    self._logger.warn(f"Database: File {path} non trovato, skip seeding.")

            if tables:
                seeder = Seeder(conn, tables, self._logger)
                result = await seeder.seed()

                if isinstance(result, Err):
                    self._logger.error(f"Database: Seeding fallito -> {result.unwrap_err()}")
                    return result

                self._logger.debug("Database: Seeding completato")

            self._connection = conn
            return Ok(True)

        except Error as e:
            exception = QueryError(
                query="Database connect",
                details=str(e)
            )
            self._logger.error(str(exception))

            if conn:
                try:
                    await conn.close()
                except Error:
                    pass

            return Err(exception)

    async def disconnect(self) -> Result[bool, ConnectionError]:
        if not self._connection:
            return Ok(True)

        try:
            await self._connection.close()
            self._logger.debug("Database: Connessione chiusa")
        except Error as e:
            exception = ConnectionError(
                self._database_url,
                action="disconnessione",
                details=str(e)
            )
            self._logger.error(str(exception))
            return Err(exception)
        finally:
            self._connection = None

        return Ok(True)