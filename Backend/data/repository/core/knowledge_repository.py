from .base import BaseRepository
from Backend.models.core.knowledges import Knowledge


class KnowledgeRepository(BaseRepository[Knowledge]):
    model = Knowledge
