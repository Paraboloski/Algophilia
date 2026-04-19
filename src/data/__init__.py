from src.data.models.souls import Soul, Trait
from src.data.models.conditions import Condition
from src.data.models.knowledges import Knowledge
from src.data.models.origins import Origin, OriginKnowledge
from src.data.models.skills import Enhanced, God, Skill, SkillFeat, SkillSpell, SkillType
from src.data.models.stats import Stat, StatAttribute, StatProgress, StatResource, StatType
from src.data.models.characters import Character, CharacterCondition, CharacterKnowledge, CharacterSkill, CharacterStat
from src.data.models.items import DamageType, Inventory, InventoryItem, Item, ItemArmor, ItemArtillery, ItemCategory, ItemMisc, WeaponType

__all__ = [
    "Condition",
    "Knowledge",
    "Trait", "Soul",
    "SkillType", "God",
    "Origin", "OriginKnowledge",
    "Enhanced", "Skill", "SkillFeat", "SkillSpell",
    "StatType", "Stat", "StatAttribute", "StatResource", "StatProgress",
    "Character", "CharacterStat", "CharacterCondition", "CharacterKnowledge", "CharacterSkill",
    "DamageType", "WeaponType", "ItemCategory", "Item", "ItemArtillery", "ItemArmor", "ItemMisc", "Inventory", "InventoryItem",
]

from src.data.templates.feats import FEATS 
from src.data.templates.spells import SPELLS 
from src.data.templates.conditions import CONDITIONS 

__all__ += ["FEATS", "SPELLS", "CONDITIONS"]

from data.repository.base import BaseRepository, eager_joinedload, sql_eq
from data.repository.condition_repository import ConditionRepository
from data.repository.knowledge_repository import KnowledgeRepository
from data.repository.soul_repository import TraitRepository, SoulRepository
from data.repository.origin_repository import OriginRepository, OriginKnowledgeRepository
from data.repository.skill_repository import EnhancedRepository, SkillRepository, SkillFeatRepository, SkillSpellRepository
from data.repository.stat_repository import StatRepository, StatAttributeRepository, StatResourceRepository, StatProgressRepository
from data.repository.item_repository import ItemRepository, ItemArtilleryRepository, ItemArmorRepository, ItemMiscRepository, InventoryRepository, InventoryItemRepository
from data.repository.character_repository import CharacterRepository, CharacterStatRepository, CharacterConditionRepository, CharacterKnowledgeRepository, CharacterSkillRepository


__all__ += [
    "BaseRepository", "eager_joinedload", "sql_eq",

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

from src.data.mysql.db import Database

__all__ += ["Database"]