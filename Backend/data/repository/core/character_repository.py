from typing import Sequence
from .base import BaseRepository
from Backend.data import Database
from Backend.config import Result, ok, err, IOError_, NotFoundError
from Backend.models import Character, CharacterStat, CharacterCondition, CharacterKnowledge, CharacterSkill


class CharacterRepository(BaseRepository[Character]):
    model = Character

    @classmethod
    def get_full(cls, character_id: int) -> Result[Character, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                from sqlalchemy.orm import joinedload
                entity = (
                    db.query(Character)
                    .options(
                        joinedload(Character.soul),
                        joinedload(Character.origin),
                        joinedload(Character.inventory),
                        joinedload(Character.stats),
                        joinedload(Character.skills),
                        joinedload(Character.conditions),
                        joinedload(Character.knowledges),
                    )
                    .filter(Character.id == character_id)
                    .first()
                )
                if entity is None:
                    return err(NotFoundError(
                        message="Character not found",
                        entity="Character",
                        identifier=character_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch full Character",
                target=str(exc),
            ))


class CharacterStatRepository(BaseRepository[CharacterStat]):
    model = CharacterStat

    @classmethod
    def get_by_id(cls, entity_id):
        raise NotImplementedError(
            "Use get_by_composite_id(character_id, stat_id) instead."
        )

    @classmethod
    def get_by_composite_id(
        cls, character_id: int, stat_id: int,
    ) -> Result[CharacterStat, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterStat, (character_id, stat_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterStat not found",
                        entity="CharacterStat",
                        identifier=(character_id, stat_id),
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch CharacterStat",
                target=str(exc),
            ))

    @classmethod
    def delete_by_composite_id(cls, character_id: int, stat_id: int,
                               ) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterStat, (character_id, stat_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterStat not found",
                        entity="CharacterStat",
                        identifier=(character_id, stat_id),
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete CharacterStat",
                target=str(exc),
            ))

    @classmethod
    def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterStat], IOError_]:
        try:
            with Database.session() as db:
                entities = (
                    db.query(CharacterStat)
                    .filter(CharacterStat.character_id == character_id)
                    .all()
                )
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list CharacterStats",
                target=str(exc),
            ))


class CharacterConditionRepository(BaseRepository[CharacterCondition]):
    model = CharacterCondition

    @classmethod
    def get_by_id(cls, entity_id):
        raise NotImplementedError(
            "Use get_by_composite_id(character_id, condition_id) instead."
        )

    @classmethod
    def get_by_composite_id(
        cls, character_id: int, condition_id: int,
    ) -> Result[CharacterCondition, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterCondition,
                                (character_id, condition_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterCondition not found",
                        entity="CharacterCondition",
                        identifier=(character_id, condition_id),
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch CharacterCondition",
                target=str(exc),
            ))

    @classmethod
    def delete_by_composite_id(
        cls, character_id: int, condition_id: int,
    ) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterCondition,
                                (character_id, condition_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterCondition not found",
                        entity="CharacterCondition",
                        identifier=(character_id, condition_id),
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete CharacterCondition",
                target=str(exc),
            ))

    @classmethod
    def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterCondition], IOError_]:
        try:
            with Database.session() as db:
                entities = (
                    db.query(CharacterCondition)
                    .filter(CharacterCondition.character_id == character_id)
                    .all()
                )
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list CharacterConditions",
                target=str(exc),
            ))


class CharacterKnowledgeRepository(BaseRepository[CharacterKnowledge]):
    model = CharacterKnowledge

    @classmethod
    def get_by_id(cls, entity_id):
        raise NotImplementedError(
            "Use get_by_composite_id(character_id, knowledge_id) instead."
        )

    @classmethod
    def get_by_composite_id(
        cls, character_id: int, knowledge_id: int,
    ) -> Result[CharacterKnowledge, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterKnowledge,
                                (character_id, knowledge_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterKnowledge not found",
                        entity="CharacterKnowledge",
                        identifier=(character_id, knowledge_id),
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch CharacterKnowledge",
                target=str(exc),
            ))

    @classmethod
    def delete_by_composite_id(
        cls, character_id: int, knowledge_id: int,
    ) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterKnowledge,
                                (character_id, knowledge_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterKnowledge not found",
                        entity="CharacterKnowledge",
                        identifier=(character_id, knowledge_id),
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete CharacterKnowledge",
                target=str(exc),
            ))

    @classmethod
    def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterKnowledge], IOError_]:
        try:
            with Database.session() as db:
                entities = (
                    db.query(CharacterKnowledge)
                    .filter(CharacterKnowledge.character_id == character_id)
                    .all()
                )
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list CharacterKnowledges",
                target=str(exc),
            ))


class CharacterSkillRepository(BaseRepository[CharacterSkill]):
    model = CharacterSkill

    @classmethod
    def get_by_id(cls, entity_id):
        raise NotImplementedError(
            "Use get_by_composite_id(character_id, skill_id) instead."
        )

    @classmethod
    def get_by_composite_id(
        cls, character_id: int, skill_id: int,
    ) -> Result[CharacterSkill, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterSkill, (character_id, skill_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterSkill not found",
                        entity="CharacterSkill",
                        identifier=(character_id, skill_id),
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch CharacterSkill",
                target=str(exc),
            ))

    @classmethod
    def delete_by_composite_id(
        cls, character_id: int, skill_id: int,
    ) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(CharacterSkill, (character_id, skill_id))
                if entity is None:
                    return err(NotFoundError(
                        message="CharacterSkill not found",
                        entity="CharacterSkill",
                        identifier=(character_id, skill_id),
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete CharacterSkill",
                target=str(exc),
            ))

    @classmethod
    def get_by_character(cls, character_id: int) -> Result[Sequence[CharacterSkill], IOError_]:
        try:
            with Database.session() as db:
                entities = (
                    db.query(CharacterSkill)
                    .filter(CharacterSkill.character_id == character_id)
                    .all()
                )
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list CharacterSkills",
                target=str(exc),
            ))
