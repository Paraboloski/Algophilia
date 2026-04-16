from .base import BaseRepository
from Backend.models.core.conditions import Condition


class ConditionRepository(BaseRepository[Condition]):
    model = Condition
