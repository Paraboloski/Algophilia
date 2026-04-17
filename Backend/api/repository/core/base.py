from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from middleware.db import Database
from typing import Any, Generic, TypeVar, Type, Sequence, cast
from middleware.config import Result, ok, err, IOError_, NotFoundError

T = TypeVar("T")


def eager_joinedload(attr: Any) -> Any:
    return joinedload(cast(Any, attr))


def sql_eq(column: Any, value: Any) -> Any:
    return cast(Any, column) == value

class BaseRepository(Generic[T]):
    model: Type[T]

    @classmethod
    def _entity_name(cls) -> str:
        return cls.model.__name__

    @classmethod
    async def create(cls, entity: T) -> Result[T, IOError_]:
        try:
            async with Database.get_async_session() as db:
                db.add(entity)
                await db.commit()
                await db.refresh(entity)
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to create {cls._entity_name()}",
                target=str(exc),
            ))

    @classmethod
    async def create_all(cls, entities: list[T]) -> Result[list[T], IOError_]:
        try:
            async with Database.get_async_session() as db:
                db.add_all(entities)
                await db.commit()
                for entity in entities:
                    await db.refresh(entity)
                    db.expunge(entity)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to bulk-create {cls._entity_name()}",
                target=str(exc),
            ))

    @classmethod
    async def get_by_id(cls, entity_id: int) -> Result[T, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                entity = await db.get(cls.model, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message=f"{cls._entity_name()} not found",
                        entity=cls._entity_name(),
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to fetch {cls._entity_name()}",
                target=str(exc),
            ))

    @classmethod
    async def get_all(cls) -> Result[Sequence[T], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(select(cls.model))
                entities = result.scalars().all()
                for entity in entities:
                    db.expunge(entity)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to list {cls._entity_name()}",
                target=str(exc),
            ))

    @classmethod
    async def update(cls, entity_id: int, data: dict) -> Result[T, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                entity = await db.get(cls.model, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message=f"{cls._entity_name()} not found",
                        entity=cls._entity_name(),
                        identifier=entity_id,
                    ))
                for key, value in data.items():
                    if hasattr(entity, key):
                        setattr(entity, key, value)
                await db.commit()
                await db.refresh(entity)
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to update {cls._entity_name()}",
                target=str(exc),
            ))

    @classmethod
    async def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                entity = await db.get(cls.model, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message=f"{cls._entity_name()} not found",
                        entity=cls._entity_name(),
                        identifier=entity_id,
                    ))
                await db.delete(entity)
                await db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to delete {cls._entity_name()}",
                target=str(exc),
            ))
