from src.data.mysql.db import Database
from result import Result
from typing import Sequence
from sqlalchemy import select
from src.config import ok, err, IOError_, NotFoundError, attempt_async
from src.data.repository.base import BaseRepository, eager_joinedload, sql_eq
from src.data.models.characters import Character, CharacterStat, CharacterCondition, CharacterKnowledge, CharacterSkill


class CharacterRepository(BaseRepository[Character]):
    model = Character

    @classmethod
    async def get_full(cls, character_id: int) -> Result[Character, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Character)
                    .options(
                        eager_joinedload(Character.soul),
                        eager_joinedload(Character.origin),
                        eager_joinedload(Character.inventory),
                        eager_joinedload(Character.stats),
                        eager_joinedload(Character.skills),
                        eager_joinedload(Character.conditions),
                        eager_joinedload(Character.knowledges),
                    )
                    .where(sql_eq(Character.id, character_id))
                )
                entity = result.scalars().unique().first()
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch full Character", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="Character not found",
                entity="Character",
                identifier=character_id,
            ))
        )


class CharacterStatRepository(BaseRepository[CharacterStat]):
    model = CharacterStat

    @classmethod
    async def get_by_composite_id(cls, character_id: int, stat_id: int) -> Result[CharacterStat, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterStat, (character_id, stat_id))
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch CharacterStat", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="CharacterStat not found",
                entity="CharacterStat",
                identifier=(character_id, stat_id),
            ))
        )

    @classmethod
    async def delete_by_composite_id(cls, character_id: int, stat_id: int) -> Result[None, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterStat, (character_id, stat_id))
                if entity is None:
                    return False
                await db.delete(entity)
                await db.commit()
                return True

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to delete CharacterStat", target=str(e))
        )

        return res.and_then(lambda deleted:
            ok(None) if deleted else
            err(NotFoundError(
                message="CharacterStat not found",
                entity="CharacterStat",
                identifier=(character_id, stat_id),
            ))
        )

    @classmethod
    async def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterStat], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(CharacterStat)
                    .where(sql_eq(CharacterStat.character_id, character_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to list CharacterStats", target=str(e))
        )


class CharacterConditionRepository(BaseRepository[CharacterCondition]):
    model = CharacterCondition
    
    @classmethod
    async def get_by_composite_id(cls, character_id: int, condition_id: int) -> Result[CharacterCondition, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterCondition, (character_id, condition_id))
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch CharacterCondition", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="CharacterCondition not found",
                entity="CharacterCondition",
                identifier=(character_id, condition_id),
            ))
        )

    @classmethod
    async def delete_by_composite_id(cls, character_id: int, condition_id: int) -> Result[None, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterCondition, (character_id, condition_id))
                if entity is None:
                    return False
                await db.delete(entity)
                await db.commit()
                return True

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to delete CharacterCondition", target=str(e))
        )

        return res.and_then(lambda deleted:
            ok(None) if deleted else
            err(NotFoundError(
                message="CharacterCondition not found",
                entity="CharacterCondition",
                identifier=(character_id, condition_id),
            ))
        )

    @classmethod
    async def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterCondition], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(CharacterCondition)
                    .where(sql_eq(CharacterCondition.character_id, character_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to list CharacterConditions", target=str(e))
        )


class CharacterKnowledgeRepository(BaseRepository[CharacterKnowledge]):
    model = CharacterKnowledge

    @classmethod
    async def get_by_composite_id(cls, character_id: int, knowledge_id: int) -> Result[CharacterKnowledge, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterKnowledge, (character_id, knowledge_id))
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch CharacterKnowledge", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="CharacterKnowledge not found",
                entity="CharacterKnowledge",
                identifier=(character_id, knowledge_id),
            ))
        )

    @classmethod
    async def delete_by_composite_id(cls, character_id: int, knowledge_id: int) -> Result[None, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterKnowledge, (character_id, knowledge_id))
                if entity is None:
                    return False
                await db.delete(entity)
                await db.commit()
                return True

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to delete CharacterKnowledge", target=str(e))
        )

        return res.and_then(lambda deleted:
            ok(None) if deleted else
            err(NotFoundError(
                message="CharacterKnowledge not found",
                entity="CharacterKnowledge",
                identifier=(character_id, knowledge_id),
            ))
        )

    @classmethod
    async def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterKnowledge], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(CharacterKnowledge)
                    .where(sql_eq(CharacterKnowledge.character_id, character_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to list CharacterKnowledges", target=str(e))
        )


class CharacterSkillRepository(BaseRepository[CharacterSkill]):
    model = CharacterSkill

    @classmethod
    async def get_by_composite_id(cls, character_id: int, skill_id: int) -> Result[CharacterSkill, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterSkill, (character_id, skill_id))
                if entity is not None:
                    db.expunge(entity)
                return entity

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch CharacterSkill", target=str(e))
        )

        return res.and_then(lambda entity:
            ok(entity) if entity is not None else
            err(NotFoundError(
                message="CharacterSkill not found",
                entity="CharacterSkill",
                identifier=(character_id, skill_id),
            ))
        )

    @classmethod
    async def delete_by_composite_id(cls, character_id: int, skill_id: int) -> Result[None, NotFoundError | IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                entity = await db.get(CharacterSkill, (character_id, skill_id))
                if entity is None:
                    return False
                await db.delete(entity)
                await db.commit()
                return True

        res = await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to delete CharacterSkill", target=str(e))
        )

        return res.and_then(lambda deleted:
            ok(None) if deleted else
            err(NotFoundError(
                message="CharacterSkill not found",
                entity="CharacterSkill",
                identifier=(character_id, skill_id),
            ))
        )

    @classmethod
    async def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterSkill], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(CharacterSkill)
                    .where(sql_eq(CharacterSkill.character_id, character_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to list CharacterSkills", target=str(e))
        )
