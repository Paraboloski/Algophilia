from .base import BaseRepository
from Backend.models import Condition


class ConditionRepository(BaseRepository[Condition]):
    model = Condition
