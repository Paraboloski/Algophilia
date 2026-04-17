from typing import Sequence

from sqlalchemy import select
from .base import BaseRepository
from Backend.api.data import Database
from middleware.assets.models.core.souls import Soul, Trait
from middleware.config import Result, ok, err, IOError_


class TraitRepository(BaseRepository[Trait]):
    model = Trait


class SoulRepository(BaseRepository[Soul]):
    model = Soul

    @classmethod
    async def get_by_trait(cls, trait_id: int) -> Result[Sequence[Soul], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Soul).where(Soul.soul_trait_id == trait_id)
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Souls by trait",
                target=str(exc),
            ))
