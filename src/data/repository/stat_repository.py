from typing import Sequence
from sqlalchemy import select
from result import Result
from src.config import ok, err, IOError_, NotFoundError, attempt_async
from src.data.mysql.db import Database
from src.data.repository.base import BaseRepository, eager_joinedload, sql_eq
from src.data.models.stats import Stat, StatAttribute, StatResource, StatProgress


class StatRepository(BaseRepository[Stat]):
    model = Stat

    @classmethod
    async def get_with_details(cls, entity_id: int) -> Result[Stat, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Stat)
                    .options(
                        eager_joinedload(Stat.attribute),
                        eager_joinedload(Stat.resource),
                        eager_joinedload(Stat.progress),
                    )
                    .where(sql_eq(Stat.id, entity_id))
                )
                entity = result.scalars().unique().first()
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Stat with details", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="Stat not found",
                entity="Stat",
                identifier=entity_id,
            ))
        )

    @classmethod
    async def get_by_type(cls, stat_type) -> Result[Sequence[Stat], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Stat).where(sql_eq(Stat.type, stat_type))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Stats by type", target=str(e))
        )


class StatAttributeRepository(BaseRepository[StatAttribute]):
    model = StatAttribute


class StatResourceRepository(BaseRepository[StatResource]):
    model = StatResource


class StatProgressRepository(BaseRepository[StatProgress]):
    model = StatProgress
