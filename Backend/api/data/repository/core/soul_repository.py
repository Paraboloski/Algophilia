from typing import Sequence

from sqlalchemy import select

from .base import BaseRepository
from Backend.api.data import Database
from Backend.api.models.core.souls import Soul, Trait
from Backend.middleware import Result, ok, err, IOError_


class TraitRepository(BaseRepository[Trait]):
    model = Trait


class SoulRepository(BaseRepository[Soul]):
    model = Soul

    @classmethod
    def get_by_trait(cls, trait_id: int) -> Result[Sequence[Soul], IOError_]:
        try:
            with Database.session() as db:
                entities = db.scalars(
                    select(Soul).where(Soul.soul_trait_id == trait_id)
                ).all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Souls by trait",
                target=str(exc),
            ))
