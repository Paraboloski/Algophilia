from typing import Sequence
from .base import BaseRepository
from Backend.data import Database
from Backend.models import Enhanced, Skill, SkillFeat, SkillSpell
from Backend.config import Result, ok, err, IOError_, NotFoundError


class EnhancedRepository(BaseRepository[Enhanced]):
    model = Enhanced


class SkillRepository(BaseRepository[Skill]):
    model = Skill

    @classmethod
    def get_with_details(cls, entity_id: int) -> Result[Skill, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                from sqlalchemy.orm import joinedload
                entity = (
                    db.query(Skill)
                    .options(
                        joinedload(Skill.Feat),
                        joinedload(Skill.Spell),
                    )
                    .filter(Skill.id == entity_id)
                    .first()
                )
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
    def get_by_type(cls, skill_type) -> Result[Sequence[Skill], IOError_]:
        """Return all skills of a given SkillType."""
        try:
            with Database.session() as db:
                entities = (
                    db.query(Skill)
                    .filter(Skill.type == skill_type)
                    .all()
                )
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Skills by type",
                target=str(exc),
            ))


class SkillFeatRepository(BaseRepository[SkillFeat]):
    model = SkillFeat

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[SkillFeat, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(SkillFeat, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="SkillFeat not found",
                        entity="SkillFeat",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch SkillFeat",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(SkillFeat, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="SkillFeat not found",
                        entity="SkillFeat",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete SkillFeat",
                target=str(exc),
            ))


class SkillSpellRepository(BaseRepository[SkillSpell]):
    model = SkillSpell

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[SkillSpell, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(SkillSpell, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="SkillSpell not found",
                        entity="SkillSpell",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch SkillSpell",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(SkillSpell, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="SkillSpell not found",
                        entity="SkillSpell",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete SkillSpell",
                target=str(exc),
            ))
