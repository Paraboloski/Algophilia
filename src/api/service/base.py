from result import Result
from src.config import IOError_, NotFoundError
from typing import Generic, TypeVar, Type, Sequence
from Backend.api.repository.core.base import BaseRepository

T = TypeVar("T")
R = TypeVar("R", bound=BaseRepository)

class BaseService(Generic[T, R]):
    repository: Type[R]

    @classmethod
    async def create(cls, entity: T) -> Result[T, IOError_]: return await cls.repository.create(entity)

    @classmethod
    async def get_by_id(cls, entity_id: int) -> Result[T, NotFoundError | IOError_]: return await cls.repository.get_by_id(entity_id)

    @classmethod
    async def get_all(cls) -> Result[Sequence[T], IOError_]: return await cls.repository.get_all()

    @classmethod
    async def update(cls, entity_id: int, data: dict) -> Result[T, NotFoundError | IOError_]: return await cls.repository.update(entity_id, data)

    @classmethod
    async def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]: return await cls.repository.delete(entity_id)
