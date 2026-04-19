from typing import Sequence
from sqlalchemy import select
from result import Result
from src.config import ok, err, IOError_, NotFoundError
from src.data import Database, BaseRepository, eager_joinedload, sql_eq, Enhanced, Skill, SkillFeat, SkillSpell

class SkillFeatRepository(BaseRepository[SkillFeat]):
    model = SkillFeat


class SkillSpellRepository(BaseRepository[SkillSpell]):
    model = SkillSpell


class EnhancedRepository(BaseRepository[Enhanced]):
    model = Enhanced

    @classmethod
    async def get_by_label(cls, label: str) -> Result[Enhanced, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Enhanced).where(sql_eq(Enhanced.label, label)).limit(1)
                )
                entity = result.scalars().first()
                if entity is None:
                    return err(NotFoundError(
                        message="Enhanced not found",
                        entity="Enhanced",
                        identifier=label,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Enhanced by label",
                target=str(exc),
            ))


class SkillRepository(BaseRepository[Skill]):
    model = Skill

    @classmethod
    async def get_by_label(cls, label: str) -> Result[Skill, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Skill).where(sql_eq(Skill.label, label)).limit(1)
                )
                entity = result.scalars().first()
                if entity is None:
                    return err(NotFoundError(
                        message="Skill not found",
                        entity="Skill",
                        identifier=label,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Skill by label",
                target=str(exc),
            ))

    @classmethod
    async def get_with_details(cls, entity_id: int) -> Result[Skill, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Skill)
                    .options(
                        eager_joinedload(Skill.feat),
                        eager_joinedload(Skill.spell),
                    )
                    .where(sql_eq(Skill.id, entity_id))
                )
                entity = result.scalars().unique().first()
                if entity is None:
                    return err(NotFoundError(
                        message="Skill not found",
                        entity="Skill",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Skill with details",
                target=str(exc),
            ))

    @classmethod
    async def get_by_type(cls, skill_type) -> Result[Sequence[Skill], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Skill).where(sql_eq(Skill.type, skill_type))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Skills by type",
                target=str(exc),
            ))