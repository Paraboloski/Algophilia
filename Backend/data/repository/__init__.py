from Backend.data.repository.core.base import BaseRepository
from Backend.data.repository.core.condition_repository import ConditionRepository
from Backend.data.repository.core.knowledge_repository import KnowledgeRepository
from Backend.data.repository.core.soul_repository import TraitRepository, SoulRepository
from Backend.data.repository.core.origin_repository import OriginRepository, OriginKnowledgeRepository
from Backend.data.repository.core.skill_repository import EnhancedRepository, SkillRepository, SkillFeatRepository, SkillSpellRepository
from Backend.data.repository.core.stat_repository import StatRepository, StatAttributeRepository, StatResourceRepository, StatProgressRepository
from Backend.data.repository.core.item_repository import ItemRepository, ItemArtilleryRepository, ItemArmorRepository, ItemMiscRepository, InventoryRepository, InventoryItemRepository
from Backend.data.repository.core.character_repository import CharacterRepository, CharacterStatRepository, CharacterConditionRepository, CharacterKnowledgeRepository, CharacterSkillRepository


__all__ = [
    "BaseRepository",

    "ConditionRepository",
    "KnowledgeRepository",

    "TraitRepository",
    "SoulRepository",

    "OriginRepository",
    "OriginKnowledgeRepository",

    "EnhancedRepository",
    "SkillRepository",
    "SkillFeatRepository",
    "SkillSpellRepository",

    "StatRepository",
    "StatAttributeRepository",
    "StatResourceRepository",
    "StatProgressRepository",

    "ItemRepository",
    "ItemArtilleryRepository",
    "ItemArmorRepository",
    "ItemMiscRepository",
    "InventoryRepository",
    "InventoryItemRepository",

    "CharacterRepository",
    "CharacterStatRepository",
    "CharacterConditionRepository",
    "CharacterKnowledgeRepository",
    "CharacterSkillRepository",
]
