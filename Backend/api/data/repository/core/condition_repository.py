from .base import BaseRepository
from Backend.api.models.core.conditions import Condition


class ConditionRepository(BaseRepository[Condition]):
    model = Condition
