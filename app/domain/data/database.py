import json
import aiosqlite
from pathlib import Path
from app.core.result import Ok, Err, Result
from app.core.exception import SchemaNotFound, ConnectionError
from app.services.load_registry import (
    feats, 
    items, 
    souls, 
    armors,
    spells, 
    weapons,
    origins, 
    conditions,
    accessories,
    knowledges, 
    weapon_tags, 
)

REGISTRY = {
    "weapon_tags": (weapon_tags, ["key", "name", "description"]),
    "feats":       (feats,       ["key", "name", "description"]),
    "origins":     (origins,     ["key", "name", "description"]),
    "conditions":  (conditions,  ["key", "name", "description"]),
    "items":       (items,       ["key", "name", "description", "weight"]),
    "knowledges":  (knowledges,  ["key", "name", "attribute", "description"]),
    "accessories": (accessories, ["key", "name", "description", "weight", "can_be_removed"]),
    "souls":       (souls,       ["key", "name", "month", "description", "soul_trait"]),
    "weapons":     (weapons,     ["key", "name", "description", "weight", "base_damage", "two_hand_damage", "weapon_tags"]),
    "spells":      (spells,      ["key", "name", "description", "affinity_with_god", "required_affinity_level", "enhanced_effect"]),
    "armors":      (armors,      ["key", "name", "description", "weight", "defence", "penalty", "slashing_defence", "blunt_defence", "piercing_defence"]),
}


class Database:
    def __init__(self, db: str | Path, schema: str | Path):
        self.db = Path(db)
        self.schema = Path(schema)
        self._conn: aiosqlite.Connection | None = None

    @property
    def connection(self) -> aiosqlite.Connection | None:
        return self._conn

    async def connect(self) -> Result[None]:
        try:
            self._conn = await aiosqlite.connect(self.db)
            self._conn.row_factory = aiosqlite.Row
            result = await self._populate()
            if not result.is_ok(): await self.close()
            return result
        except Exception as e:
            return Err(ConnectionError(f"Connessione fallita: {e}"))

    async def _populate(self) -> Result[None]:
        if self._conn is None: return Err(ConnectionError("Non connesso"))
        if not self.schema.exists(): return Err(SchemaNotFound(self.schema))
        try:
            await self._conn.executescript(self.schema.read_text(encoding="utf-8"))
            await self._conn.commit()
            return Ok(None)
        except Exception as e:
            return Err(ConnectionError(f"Schema: {e}"))

    async def _table_exists(self, table: str) -> bool:
        if self._conn is None: return False
        async with self._conn.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", 
                (table,)
            ) as query:
            return await query.fetchone() is not None

    async def _is_table_empty(self, table: str) -> bool:
        if self._conn is None:
            return True
        async with self._conn.execute(f"SELECT count(*) FROM {table}") as cursor:
            row = await cursor.fetchone()
            return row[0] == 0 if row else True

    async def seed(self) -> Result[None]:
        if self._conn is None:
            return Err(ConnectionError("Non connesso"))
        try:
            for table, (registry, columns) in REGISTRY.items():
                if not await self._table_exists(table):
                    return Err(ConnectionError(f"Tabella '{table}' non trovata — schema non applicato?"))
                
                if not await self._is_table_empty(table): continue
                if not registry: continue

                placeholders = ", ".join("?" * len(columns))
                sql = (
                    f"INSERT OR IGNORE INTO {table} ({', '.join(columns)}) " f"VALUES ({placeholders})")
                rows = [
                    tuple(self._extract(model, column) for column in columns)
                    for model in registry.values()
                ]
                await self._conn.executemany(sql, rows)
            await self._conn.commit()
            return Ok(None)
        except Exception as e:
            return Err(ConnectionError(f"Seed fallito: {e}"))

    def _extract(self, model, column: str):
        value = getattr(model, column, None)
        
        if value is None: return None
        if hasattr(value, "value"): return value.value
        if isinstance(value, (list, dict)): return json.dumps(value)
        if hasattr(value, "model_dump"): return json.dumps(value.model_dump())
        
        return value

    async def close(self) -> None:
        if self._conn:
            await self._conn.close()
            self._conn = None

    async def commit(self) -> Result[None]:
        if self._conn is None:
            return Err(ConnectionError("Non connesso"))
        try:
            await self._conn.commit()
            return Ok(None)
        except Exception as e:
            return Err(ConnectionError(f"Commit fallito: {e}"))
