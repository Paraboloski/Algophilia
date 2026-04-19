from typing import Sequence
from sqlalchemy import select
from result import Result
from src.config import ok, err, IOError_, NotFoundError, attempt_async
from src.data.mysql.db import Database
from src.data.models.origins import Origin, OriginKnowledge
from src.data.repository.base import BaseRepository, eager_joinedload, sql_eq

class OriginRepository(BaseRepository[Origin]):
    model = Origin

    @classmethod
    async def get_with_knowledges(cls, origin_id: int) -> Result[Origin, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Origin)
                    .options(eager_joinedload(Origin.knowledges))
                    .where(sql_eq(Origin.id, origin_id))
                )
                entity = result.scalars().unique().first()
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Origin with knowledges", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="Origin not found",
                entity="Origin",
                identifier=origin_id,
            ))
        )


class OriginKnowledgeRepository(BaseRepository[OriginKnowledge]):
    model = OriginKnowledge

    @classmethod
    async def get_by_composite_id(cls, origin_id: int, knowledge_id: int) -> Result[OriginKnowledge, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(OriginKnowledge, (origin_id, knowledge_id))
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch OriginKnowledge", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="OriginKnowledge not found",
                entity="OriginKnowledge",
                identifier=(origin_id, knowledge_id),
            ))
        )

    @classmethod
    async def delete_by_composite_id(cls, origin_id: int, knowledge_id: int) -> Result[None, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(OriginKnowledge, (origin_id, knowledge_id))
                if entity is None:
                    return False
                await db.delete(entity)
                await db.commit()
                return True

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to delete OriginKnowledge", target=str(e))
        )

        return res.and_then(lambda deleted:
            ok(None) if deleted else
            err(NotFoundError(
                message="OriginKnowledge not found",
                entity="OriginKnowledge",
                identifier=(origin_id, knowledge_id),
            ))
        )

    @classmethod
    async def get_by_origin(cls, origin_id: int) -> Result[Sequence[OriginKnowledge], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(OriginKnowledge)
                    .where(sql_eq(OriginKnowledge.origin_id, origin_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to list OriginKnowledges by origin", target=str(e))
        )
