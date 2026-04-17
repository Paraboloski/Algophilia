from typing import Sequence
from middleware.config import Result, IOError_
from middleware.assets.models.core.items import Item
from middleware.assets.models.core.stats import Stat
from middleware.assets.models.core.skills import Skill
from middleware.assets.models.core.origins import Origin
from middleware.assets.models.core.souls import Soul, Trait
from middleware.assets.models.core.knowledges import Knowledge
from middleware.assets.models.core.conditions import Condition
from Backend.api.repository import SkillRepository, OriginRepository, SoulRepository, TraitRepository, ItemRepository, StatRepository, KnowledgeRepository, ConditionRepository


class ReferenceService:
    @classmethod
    async def get_all_skills(cls) -> Result[Sequence[Skill], IOError_]: return await SkillRepository.get_all()

    @classmethod
    async def get_all_origins(cls) -> Result[Sequence[Origin], IOError_]: return await OriginRepository.get_all()

    @classmethod
    async def get_all_souls(cls) -> Result[Sequence[Soul], IOError_]: return await SoulRepository.get_all()

    @classmethod
    async def get_all_traits(cls) -> Result[Sequence[Trait], IOError_]: return await TraitRepository.get_all()

    @classmethod
    async def get_all_items(cls) -> Result[Sequence[Item], IOError_]: return await ItemRepository.get_all()

    @classmethod
    async def get_all_stats(cls) -> Result[Sequence[Stat], IOError_]: return await StatRepository.get_all()

    @classmethod
    async def get_all_knowledges(cls) -> Result[Sequence[Knowledge], IOError_]: return await KnowledgeRepository.get_all()

    @classmethod
    async def get_all_conditions(cls) -> Result[Sequence[Condition], IOError_]: return await ConditionRepository.get_all()
