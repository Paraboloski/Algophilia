from src.data.models.conditions import Condition
from src.data.repository.base import BaseRepository


class ConditionRepository(BaseRepository[Condition]):
    model = Condition
