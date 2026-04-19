from src.data import Knowledge, BaseRepository


class KnowledgeRepository(BaseRepository[Knowledge]):
    model = Knowledge
