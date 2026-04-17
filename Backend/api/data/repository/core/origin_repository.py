from typing import Sequence
from sqlalchemy import select
from .base import BaseRepository
from Backend.api.data import Database
from sqlalchemy.orm import joinedload
from Backend.api.models.core.origins import Origin, OriginKnowledge
from Backend.middleware import Result, ok, err, IOError_, NotFoundError


class OriginRepository(BaseRepository[Origin]):
    model = Origin

    @classmethod
    def get_with_knowledges(cls, origin_id: int) -> Result[Origin, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.scalars(
                    select(Origin)
                    .options(joinedload(Origin.knowledges))
                    .where(Origin.id == origin_id)
                ).first()
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
    def get_by_composite_id(cls, origin_id: int, knowledge_id: int) -> Result[OriginKnowledge, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(OriginKnowledge, (origin_id, knowledge_id))
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
    def delete_by_composite_id(cls, origin_id: int, knowledge_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(OriginKnowledge, (origin_id, knowledge_id))
                if entity is None:
                    return err(NotFoundError(
                        message="OriginKnowledge not found",
                        entity="OriginKnowledge",
                        identifier=(origin_id, knowledge_id),
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete OriginKnowledge",
                target=str(exc),
            ))

    @classmethod
    def get_by_origin(cls, origin_id: int) -> Result[Sequence[OriginKnowledge], IOError_]:
        try:
            with Database.session() as db:
                entities = db.scalars(
                    select(OriginKnowledge)
                    .where(OriginKnowledge.origin_id == origin_id)
                ).all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list OriginKnowledges by origin",
                target=str(exc),
            ))
