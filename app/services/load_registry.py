from pathlib import Path
from yaml import safe_load
from pydantic import BaseModel
from app.config import settings
from typing import TypeVar, Type

from app.domain import (
    Item,
    Soul,
    Feat,
    Spell,
    Armor,
    Weapon,
    Origin,
    WeaponTag,
    Accessory,
    Knowledge,
    Condition,
)

feats:        dict[str, Feat] = {}
items:        dict[str, Item] = {}
souls:        dict[str, Soul] = {}
spells:       dict[str, Spell] = {}
armors:       dict[str, Armor] = {}
weapons:      dict[str, Weapon] = {}
origins:      dict[str, Origin] = {}
weapon_tags:  dict[str, WeaponTag] = {}
accessories:  dict[str, Accessory] = {}
knowledges:   dict[str, Knowledge] = {}
conditions:   dict[str, Condition] = {}

T = TypeVar("T", bound=BaseModel)

def load_registry(path: Path, model: Type[T], key: str | None = None) -> dict[str, T]:
    if not path.exists(): return {}
        
    raw = safe_load(path.read_text(encoding="utf-8")) or {}
    data = raw.get(key, raw) if key else raw
        
    if isinstance(data, dict): return {k: model.model_validate({"key": k, **v}) for k, v in data.items()}
    if isinstance(data, list): return {item.get("key", ""): model.model_validate(item) for item in data if item}
        
    return {}


def load_all() -> None:
    items.update(load_registry(settings.STATIC_ITEM_PATH, Item, "items"))
    souls.update(load_registry(settings.STATIC_SOUL_PATH, Soul, "souls"))
    feats.update(load_registry(settings.STATIC_SKILL_PATH, Feat, "feats"))
    armors.update(load_registry(settings.STATIC_ITEM_PATH, Armor, "armors"))
    spells.update(load_registry(settings.STATIC_SKILL_PATH, Spell, "spells"))
    weapons.update(load_registry(settings.STATIC_ITEM_PATH, Weapon, "weapons"))
    origins.update(load_registry(settings.STATIC_ORIGIN_PATH, Origin, "origins"))
    accessories.update(load_registry(settings.STATIC_ITEM_PATH, Accessory, "accessories"))
    knowledges.update(load_registry(settings.STATIC_KNOWLEDGE_PATH, Knowledge, "knowledges"))
    conditions.update(load_registry(settings.STATIC_CONDITION_PATH, Condition, "conditions"))
    weapon_tags.update(load_registry(settings.STATIC_WEAPON_TAG_PATH, WeaponTag, "weapon_tags"))
