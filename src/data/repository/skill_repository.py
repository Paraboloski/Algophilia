from typing import Sequence
from sqlalchemy import select
from result import Result
from src.config import ok, err, IOError_, NotFoundError, attempt_async
from src.data.mysql.db import Database
from src.data.repository.base import BaseRepository, eager_joinedload, sql_eq
from src.data.models.skills import Enhanced, Skill, SkillFeat, SkillSpell

class SkillFeatRepository(BaseRepository[SkillFeat]):
    model = SkillFeat


class SkillSpellRepository(BaseRepository[SkillSpell]):
    model = SkillSpell


class EnhancedRepository(BaseRepository[Enhanced]):
    model = Enhanced

    @classmethod
    async def get_by_label(cls, label: str) -> Result[Enhanced, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Enhanced).where(sql_eq(Enhanced.label, label)).limit(1)
                )
                entity = result.scalars().first()
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Enhanced by label", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="Enhanced not found",
                entity="Enhanced",
                identifier=label,
            ))
        )


class SkillRepository(BaseRepository[Skill]):
    model = Skill

    @classmethod
    async def get_by_label(cls, label: str) -> Result[Skill, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Skill).where(sql_eq(Skill.label, label)).limit(1)
                )
                entity = result.scalars().first()
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Skill by label", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="Skill not found",
                entity="Skill",
                identifier=label,
            ))
        )

    @classmethod
    async def get_with_details(cls, entity_id: int) -> Result[Skill, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Skill)
                    .options(
                        eager_joinedload(Skill.feat),
                        eager_joinedload(Skill.spell),
                    )
                    .where(sql_eq(Skill.id, entity_id))
                )
                entity = result.scalars().unique().first()
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Skill with details", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="Skill not found",
                entity="Skill",
                identifier=entity_id,
            ))
        )

    @classmethod
    async def get_by_type(cls, skill_type) -> Result[Sequence[Skill], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Skill).where(sql_eq(Skill.type, skill_type))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Skills by type", target=str(e))
        )