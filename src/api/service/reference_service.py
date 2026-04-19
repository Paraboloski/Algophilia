from result import Result
from typing import Sequence
from src.config import IOError_
from src.data import Item, Stat, Skill, Origin, Soul, Trait, Knowledge, Condition, SkillRepository, OriginRepository, SoulRepository, TraitRepository, ItemRepository, StatRepository, KnowledgeRepository, ConditionRepository

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
