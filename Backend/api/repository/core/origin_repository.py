from typing import Sequence
from sqlalchemy import select
from middleware.db import Database
from .base import BaseRepository, eager_joinedload, sql_eq
from middleware.assets.models.core.origins import Origin, OriginKnowledge
from middleware.config import Result, ok, err, IOError_, NotFoundError


class OriginRepository(BaseRepository[Origin]):
    model = Origin

    @classmethod
    async def get_with_knowledges(cls, origin_id: int) -> Result[Origin, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Origin)
                    .options(eager_joinedload(Origin.knowledges))
                    .where(sql_eq(Origin.id, origin_id))
                )
                entity = result.scalars().unique().first()
                if entity is None:
                    return err(NotFoundError(
                        message="Origin not found",
                        entity="Origin",
                        identifier=origin_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Origin with knowledges",
                target=str(exc),
            ))


class OriginKnowledgeRepository(BaseRepository[OriginKnowledge]):
    model = OriginKnowledge

    @classmethod
    async def get_by_composite_id(cls, origin_id: int, knowledge_id: int) -> Result[OriginKnowledge, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                entity = await db.get(OriginKnowledge, (origin_id, knowledge_id))
                if entity is None:
                    return err(NotFoundError(
                        message="OriginKnowledge not found",
                        entity="OriginKnowledge",
                        identifier=(origin_id, knowledge_id),
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch OriginKnowledge",
                target=str(exc),
            ))

    @classmethod
    async def delete_by_composite_id(cls, origin_id: int, knowledge_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                entity = await db.get(OriginKnowledge, (origin_id, knowledge_id))
                if entity is None:
                    return err(NotFoundError(
                        message="OriginKnowledge not found",
                        entity="OriginKnowledge",
                        identifier=(origin_id, knowledge_id),
                    ))
                await db.delete(entity)
                await db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete OriginKnowledge",
                target=str(exc),
            ))

    @classmethod
    async def get_by_origin(cls, origin_id: int) -> Result[Sequence[OriginKnowledge], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(OriginKnowledge)
                    .where(sql_eq(OriginKnowledge.origin_id, origin_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list OriginKnowledges by origin",
                target=str(exc),
            ))
