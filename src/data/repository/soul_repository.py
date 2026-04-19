from typing import Sequence
from sqlalchemy import select
from result import Result
from src.config import ok, err, IOError_, attempt_async
from src.data.mysql.db import Database
from src.data.models.souls import Soul, Trait
from src.data.repository.base import BaseRepository, sql_eq

class TraitRepository(BaseRepository[Trait]):
    model = Trait

class SoulRepository(BaseRepository[Soul]):
    model = Soul

    @classmethod
    async def get_by_trait(cls, trait_id: int) -> Result[Sequence[Soul], IOError_]:
        async def _run():
            async with Database._get_async_session() as db:
                result = await db.execute(
                    select(Soul).where(sql_eq(Soul.soul_trait_id, trait_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return entities

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Failed to fetch Souls by trait", target=str(e))
        )
