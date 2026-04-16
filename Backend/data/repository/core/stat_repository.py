from typing import Sequence
from .base import BaseRepository
from Backend.data import Database
from Backend.config import Result, ok, err, IOError_, NotFoundError
from Backend.models import Stat, StatAttribute, StatResource, StatProgress


class StatRepository(BaseRepository[Stat]):
    model = Stat

    @classmethod
    def get_with_details(cls, entity_id: int) -> Result[Stat, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                from sqlalchemy.orm import joinedload
                entity = (
                    db.query(Stat)
                    .options(
                        joinedload(Stat.Attribute),
                        joinedload(Stat.Resource),
                        joinedload(Stat.Progress),
                    )
                    .filter(Stat.id == entity_id)
                    .first()
                )
                if entity is None:
                    return err(NotFoundError(
                        message="Stat not found",
                        entity="Stat",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Stat with details",
                target=str(exc),
            ))

    @classmethod
    def get_by_type(cls, stat_type) -> Result[Sequence[Stat], IOError_]:
        try:
            with Database.session() as db:
                entities = (
                    db.query(Stat)
                    .filter(Stat.type == stat_type)
                    .all()
                )
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Stats by type",
                target=str(exc),
            ))


class StatAttributeRepository(BaseRepository[StatAttribute]):
    model = StatAttribute

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[StatAttribute, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(StatAttribute, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="StatAttribute not found",
                        entity="StatAttribute",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch StatAttribute",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(StatAttribute, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="StatAttribute not found",
                        entity="StatAttribute",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete StatAttribute",
                target=str(exc),
            ))


class StatResourceRepository(BaseRepository[StatResource]):
    model = StatResource

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[StatResource, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(StatResource, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="StatResource not found",
                        entity="StatResource",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch StatResource",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(StatResource, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="StatResource not found",
                        entity="StatResource",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete StatResource",
                target=str(exc),
            ))


class StatProgressRepository(BaseRepository[StatProgress]):
    model = StatProgress

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[StatProgress, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(StatProgress, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="StatProgress not found",
                        entity="StatProgress",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch StatProgress",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(StatProgress, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="StatProgress not found",
                        entity="StatProgress",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete StatProgress",
                target=str(exc),
            ))
