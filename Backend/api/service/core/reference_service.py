from typing import Sequence
from Backend.api.models.core.items import Item
from Backend.api.models.core.stats import Stat
from Backend.middleware import Result, IOError_
from Backend.api.models.core.skills import Skill
from Backend.api.models.core.origins import Origin
from Backend.api.models.core.souls import Soul, Trait
from Backend.api.models.core.knowledges import Knowledge
from Backend.api.models.core.conditions import Condition
from Backend.api.data.repository import SkillRepository, OriginRepository, SoulRepository, TraitRepository, ItemRepository, StatRepository, KnowledgeRepository, ConditionRepository


class ReferenceService:
    @classmethod
    def get_all_skills(cls) -> Result[Sequence[Skill], IOError_]: return SkillRepository.get_all()

    @classmethod
    def get_all_origins(cls) -> Result[Sequence[Origin], IOError_]: return OriginRepository.get_all()

    @classmethod
    def get_all_souls(cls) -> Result[Sequence[Soul], IOError_]: return SoulRepository.get_all()

    @classmethod
    def get_all_traits(cls) -> Result[Sequence[Trait], IOError_]: return TraitRepository.get_all()

    @classmethod
    def get_all_items(cls) -> Result[Sequence[Item], IOError_]: return ItemRepository.get_all()

    @classmethod
    def get_all_stats(cls) -> Result[Sequence[Stat], IOError_]: return StatRepository.get_all()

    @classmethod
    def get_all_knowledges(cls) -> Result[Sequence[Knowledge], IOError_]: return KnowledgeRepository.get_all()

    @classmethod
    def get_all_conditions(cls) -> Result[Sequence[Condition], IOError_]: return ConditionRepository.get_all()
