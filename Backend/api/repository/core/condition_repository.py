from Backend.api.repository.core.base import BaseRepository
from middleware.assets.models.core.conditions import Condition


class ConditionRepository(BaseRepository[Condition]):
    model = Condition
