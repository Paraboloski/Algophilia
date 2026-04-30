from aiosqlite import Error, Connection
from result import Ok, Err, Result

from app.data.database import Database
from app.events.logger import Logger
from app.utils.exception import AppError, QueryError


class Repository:
    def __init__(self, database: Database, logger: Logger) -> None:
        self._logger = logger
        self._database = database

    def get_connection(self) -> Result[Connection, AppError]:
        return self._database.get_connection()

    async def execute(self, query: str, params: tuple = ()) -> Result[bool, AppError]:
        conn_result = self.get_connection()
        if conn_result.is_err():
            return Err(conn_result.unwrap_err())

        conn = conn_result.unwrap()

        try:
            self._logger.debug(f"SQL: {query} | Params: {params}")

            await conn.execute(query, params)
            await conn.commit()

            return Ok(True)

        except Error as e:
            await conn.rollback()

            exception = QueryError(query=query, details=str(e))
            self._logger.error(str(exception))

            return Err(exception)

    async def execute_all(self, queries: list[tuple[str, tuple]]) -> Result[bool, AppError]:
        conn_result = self.get_connection()
        if conn_result.is_err():
            return Err(conn_result.unwrap_err())

        conn = conn_result.unwrap()

        try:
            for query, params in queries:
                self._logger.debug(f"SQL: {query} | Params: {params}")
                await conn.execute(query, params)

            await conn.commit()
            return Ok(True)

        except Error as e:
            await conn.rollback()

            exception = QueryError(query="BATCH_EXECUTE", details=str(e))
            self._logger.error(str(exception))

            return Err(exception)