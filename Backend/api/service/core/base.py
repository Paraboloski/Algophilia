from typing import Generic, TypeVar, Type, Sequence
from Backend.middleware import Result, IOError_, NotFoundError
from Backend.api.data.repository.core.base import BaseRepository

T = TypeVar("T")
R = TypeVar("R", bound=BaseRepository)

class BaseService(Generic[T, R]):
    repository: Type[R]

    @classmethod
    def create(cls, entity: T) -> Result[T, IOError_]: return cls.repository.create(entity)

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[T, NotFoundError | IOError_]: return cls.repository.get_by_id(entity_id)

    @classmethod
    def get_all(cls) -> Result[Sequence[T], IOError_]: return cls.repository.get_all()

    @classmethod
    def update(cls, entity_id: int, data: dict) -> Result[T, NotFoundError | IOError_]: return cls.repository.update(entity_id, data)

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]: return cls.repository.delete(entity_id)
