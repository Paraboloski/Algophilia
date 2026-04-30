import json
from pathlib import Path
from yaml import safe_load
from result import Ok, Err, Result
from app.events.logger import Logger
from aiosqlite import Connection, Error
from app.utils.exception import AppError, QueryError


class Seeder:
    def __init__(self, connection: Connection, tables: dict[str, Path], logger: Logger) -> None:
        self._tables = tables
        self._logger = logger
        self._connection = connection

    def normalize(self, row: dict) -> tuple[list[str], list]:
        cleaned = {}

        for key, value in row.items():
            if isinstance(value, (list, dict)):
                cleaned[key] = json.dumps(value)
            else:
                cleaned[key] = value

        columns = list(cleaned.keys())
        values = list(cleaned.values())

        return columns, values

    async def seed(self) -> Result[bool, AppError]:
        inserted = 0
        skipped = 0

        for table, path in self._tables.items():

            try:
                script = Path(path).read_text(encoding="utf-8")
                rows = safe_load(script)
            except Exception as e:
                self._logger.error(f"Seeder: errore lettura {table}: {e}")
                skipped += 1
                continue

            if not rows:
                self._logger.warn(f"Seeder: tabella vuota {table}")
                continue
            
            try:
                cursor = await self._connection.execute(f"SELECT COUNT(*) FROM {table}")
                row = await cursor.fetchone()
                if row and row[0] > 0:
                    self._logger.debug(f"Seeder: {table} già popolata ({row[0]} righe), skip")
                    continue
            except Error as e:
                self._logger.error(f"Seeder: errore controllo {table} -> {e}")
                skipped += 1
                continue

    
            table_count = 0

            for row in rows:
                try:
                    columns, values = self.normalize(row)

                    placeholders = ", ".join(["?"] * len(values))
                    columns_sql = ", ".join(columns)

                    query = (
                        f"INSERT OR IGNORE INTO {table} " 
                        f"({columns_sql}) VALUES ({placeholders})"
                    )

                    before = self._connection.total_changes        
                    await self._connection.execute(query, tuple(values))
                    
                    if self._connection.total_changes > before:  
                        table_count += 1
                    else:
                        skipped += 1

                except Error as e:
                    skipped += 1
                    self._logger.error(f"Seeder: errore SQL {table} -> {e}")

            inserted += table_count
            self._logger.debug(f"Seeder: {table} -> {table_count} inserite, {skipped} skippate")

        try:
            await self._connection.commit()
        except Error as e:
            return Err(QueryError("SEED_COMMIT", str(e)))

        self._logger.debug(f"Seeder completato: inserted={inserted}, skipped={skipped}")
        return Ok(True)