from Backend.models import Knowledge
from .base import BaseRepository


class KnowledgeRepository(BaseRepository[Knowledge]):
    model = Knowledge
