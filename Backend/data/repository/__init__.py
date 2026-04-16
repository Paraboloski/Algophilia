from Backend.data.repository.base import BaseRepository

from Backend.data.repository.condition_repository import ConditionRepository
from Backend.data.repository.knowledge_repository import KnowledgeRepository

from Backend.data.repository.soul_repository import TraitRepository, SoulRepository

from Backend.data.repository.origin_repository import (
    OriginRepository, OriginKnowledgeRepository,
)

from Backend.data.repository.skill_repository import (
    EnhancedRepository, SkillRepository,
    SkillFeatRepository, SkillSpellRepository,
)

from Backend.data.repository.stat_repository import (
    StatRepository, StatAttributeRepository,
    StatResourceRepository, StatProgressRepository,
)

from Backend.data.repository.item_repository import (
    ItemRepository, ItemArtilleryRepository,
    ItemArmorRepository, ItemMiscRepository,
    InventoryRepository, InventoryItemRepository,
)

from Backend.data.repository.character_repository import (
    CharacterRepository,
    CharacterStatRepository,
    CharacterConditionRepository,
    CharacterKnowledgeRepository,
    CharacterSkillRepository,
)

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
