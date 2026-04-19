from src.data.models.knowledges import Knowledge
from src.data.repository.base import BaseRepository


class KnowledgeRepository(BaseRepository[Knowledge]):
    model = Knowledge
