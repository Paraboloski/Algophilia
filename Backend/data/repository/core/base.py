
from __future__ import annotations

from sqlalchemy.orm import Session
from typing import Generic, TypeVar, Type, Sequence

from Backend.data import Database
from Backend.config import Result, ok, err, IOError_, NotFoundError

T = TypeVar("T")


class BaseRepository(Generic[T]):
    model: Type[T]

    @classmethod
    def _entity_name(cls) -> str:
        return cls.model.__name__

    @classmethod
    def create(cls, entity: T) -> Result[T, IOError_]:
        try:
            with Database.session() as db:
                db.add(entity)
                db.commit()
                db.refresh(entity)
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to create {cls._entity_name()}",
                target=str(exc),
            ))

    @classmethod
    def create_all(cls, entities: list[T]) -> Result[list[T], IOError_]:
        """Bulk-insert a list of entities."""
        try:
            with Database.session() as db:
                db.add_all(entities)
                db.commit()
                for entity in entities:
                    db.refresh(entity)
                    db.expunge(entity)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to bulk-create {cls._entity_name()}",
                target=str(exc),
            ))

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[T, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(cls.model, entity_id)
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
    def get_all(cls) -> Result[Sequence[T], IOError_]:
        try:
            with Database.session() as db:
                entities = db.query(cls.model).all()
                for entity in entities:
                    db.expunge(entity)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to list {cls._entity_name()}",
                target=str(exc),
            ))


    @classmethod
    def update(cls, entity_id: int, data: dict) -> Result[T, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(cls.model, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message=f"{cls._entity_name()} not found",
                        entity=cls._entity_name(),
                        identifier=entity_id,
                    ))
                for key, value in data.items():
                    if hasattr(entity, key):
                        setattr(entity, key, value)
                db.commit()
                db.refresh(entity)
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to update {cls._entity_name()}",
                target=str(exc),
            ))


    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(cls.model, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message=f"{cls._entity_name()} not found",
                        entity=cls._entity_name(),
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message=f"Failed to delete {cls._entity_name()}",
                target=str(exc),
            ))
