from typing import Sequence
from sqlalchemy import select
from .base import BaseRepository
from Backend.api.data import Database
from sqlalchemy.orm import joinedload
from middleware.config import Result, ok, err, IOError_, NotFoundError
from middleware.assets.models.core.stats import Stat, StatAttribute, StatResource, StatProgress


class StatRepository(BaseRepository[Stat]):
    model = Stat

    @classmethod
    async def get_with_details(cls, entity_id: int) -> Result[Stat, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Stat)
                    .options(
                        joinedload(Stat.attribute),
                        joinedload(Stat.resource),
                        joinedload(Stat.progress),
                    )
                    .where(Stat.id == entity_id)
                )
                entity = result.scalars().unique().first()
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
    async def get_by_type(cls, stat_type) -> Result[Sequence[Stat], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Stat).where(Stat.type == stat_type)
                )
                entities = result.scalars().all()
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


class StatResourceRepository(BaseRepository[StatResource]):
    model = StatResource


class StatProgressRepository(BaseRepository[StatProgress]):
    model = StatProgress
