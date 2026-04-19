from src.data import Condition, BaseRepository


class ConditionRepository(BaseRepository[Condition]):
    model = Condition
