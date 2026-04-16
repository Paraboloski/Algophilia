from typing import Sequence
from sqlalchemy import select
from .base import BaseRepository
from Backend.data import Database
from sqlalchemy.orm import joinedload
from Backend.models.core.skills import Enhanced, Skill, SkillFeat, SkillSpell
from Backend.config import Result, ok, err, IOError_, NotFoundError


class EnhancedRepository(BaseRepository[Enhanced]):
    model = Enhanced


class SkillRepository(BaseRepository[Skill]):
    model = Skill

    @classmethod
    def get_with_details(cls, entity_id: int) -> Result[Skill, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.scalars(
                    select(Skill)
                    .options(
                        joinedload(Skill.feat),
                        joinedload(Skill.spell),
                    )
                    .where(Skill.id == entity_id)
                ).first()
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
        try:
            with Database.session() as db:
                entities = db.scalars(
                    select(Skill).where(Skill.type == skill_type)
                ).all()
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


class SkillSpellRepository(BaseRepository[SkillSpell]):
    model = SkillSpell
