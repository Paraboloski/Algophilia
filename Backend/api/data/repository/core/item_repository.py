from typing import Sequence
from sqlalchemy import select
from .base import BaseRepository
from Backend.api.data import Database
from sqlalchemy.orm import joinedload
from Backend.middleware import Result, ok, err, IOError_, NotFoundError
from Backend.api.models.core.items import Item, ItemArtillery, ItemArmor, ItemMisc, Inventory, InventoryItem


class ItemRepository(BaseRepository[Item]):
    model = Item

    @classmethod
    def get_with_details(cls, entity_id: int) -> Result[Item, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.scalars(
                    select(Item)
                    .options(
                        joinedload(Item.artillery),
                        joinedload(Item.armor),
                        joinedload(Item.misc),
                    )
                    .where(Item.id == entity_id)
                ).first()
                if entity is None:
                    return err(NotFoundError(
                        message="Item not found",
                        entity="Item",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Item with details",
                target=str(exc),
            ))

    @classmethod
    def get_by_category(cls, category) -> Result[Sequence[Item], IOError_]:
        try:
            with Database.session() as db:
                entities = db.scalars(
                    select(Item).where(Item.category == category)
                ).all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Items by category",
                target=str(exc),
            ))


class ItemArtilleryRepository(BaseRepository[ItemArtillery]):
    model = ItemArtillery


class ItemArmorRepository(BaseRepository[ItemArmor]):
    model = ItemArmor


class ItemMiscRepository(BaseRepository[ItemMisc]):
    model = ItemMisc


class InventoryRepository(BaseRepository[Inventory]):
    model = Inventory

    @classmethod
    def get_by_character(cls, character_id: int) -> Result[Inventory, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.scalars(
                    select(Inventory)
                    .options(joinedload(Inventory.items))
                    .where(Inventory.character_id == character_id)
                ).first()
                if entity is None:
                    return err(NotFoundError(
                        message="Inventory not found for character",
                        entity="Inventory",
                        identifier=character_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Inventory by character",
                target=str(exc),
            ))


class InventoryItemRepository(BaseRepository[InventoryItem]):
    model = InventoryItem

    @classmethod
    def get_by_inventory(cls, inventory_id: int) -> Result[Sequence[InventoryItem], IOError_]:
        try:
            with Database.session() as db:
                entities = db.scalars(
                    select(InventoryItem)
                    .where(InventoryItem.inventory_id == inventory_id)
                ).all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list InventoryItems",
                target=str(exc),
            ))
