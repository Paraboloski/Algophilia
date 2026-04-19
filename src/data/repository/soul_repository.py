from typing import Sequence
from sqlalchemy import select
from result import Result
from src.config import ok, err, IOError_
from src.data import Database, Soul, Trait, BaseRepository, sql_eq

class TraitRepository(BaseRepository[Trait]):
    model = Trait

class SoulRepository(BaseRepository[Soul]):
    model = Soul

    @classmethod
    async def get_by_trait(cls, trait_id: int) -> Result[Sequence[Soul], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Soul).where(sql_eq(Soul.soul_trait_id, trait_id))
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
