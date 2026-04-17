from .base import BaseRepository
from middleware.assets.models.core.knowledges import Knowledge


class KnowledgeRepository(BaseRepository[Knowledge]):
    model = Knowledge
