from .base import BaseRepository
from Backend.api.models.core.knowledges import Knowledge


class KnowledgeRepository(BaseRepository[Knowledge]):
    model = Knowledge
