from typing import Sequence
from .base import BaseRepository
from Backend.data import Database
from Backend.models import Item, ItemArtillery, ItemArmor, ItemMisc, Inventory, InventoryItem
from Backend.config import Result, ok, err, IOError_, NotFoundError


class ItemRepository(BaseRepository[Item]):
    model = Item

    @classmethod
    def get_with_details(cls, entity_id: int) -> Result[Item, NotFoundError | IOError_]:
        """Fetch an Item eagerly loading artillery / armor / misc."""
        try:
            with Database.session() as db:
                from sqlalchemy.orm import joinedload
                entity = (
                    db.query(Item)
                    .options(
                        joinedload(Item.artillery),
                        joinedload(Item.armor),
                        joinedload(Item.misc),
                    )
                    .filter(Item.id == entity_id)
                    .first()
                )
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
        """Return all items of a given ItemCategory."""
        try:
            with Database.session() as db:
                entities = (
                    db.query(Item)
                    .filter(Item.category == category)
                    .all()
                )
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

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[ItemArtillery, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(ItemArtillery, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="ItemArtillery not found",
                        entity="ItemArtillery",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch ItemArtillery",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(ItemArtillery, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="ItemArtillery not found",
                        entity="ItemArtillery",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete ItemArtillery",
                target=str(exc),
            ))


class ItemArmorRepository(BaseRepository[ItemArmor]):
    """Sub-record keyed by entity_id."""
    model = ItemArmor

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[ItemArmor, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(ItemArmor, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="ItemArmor not found",
                        entity="ItemArmor",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch ItemArmor",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(ItemArmor, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="ItemArmor not found",
                        entity="ItemArmor",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete ItemArmor",
                target=str(exc),
            ))


class ItemMiscRepository(BaseRepository[ItemMisc]):
    """Sub-record keyed by entity_id."""
    model = ItemMisc

    @classmethod
    def get_by_id(cls, entity_id: int) -> Result[ItemMisc, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(ItemMisc, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="ItemMisc not found",
                        entity="ItemMisc",
                        identifier=entity_id,
                    ))
                db.expunge(entity)
                return ok(entity)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch ItemMisc",
                target=str(exc),
            ))

    @classmethod
    def delete(cls, entity_id: int) -> Result[None, NotFoundError | IOError_]:
        try:
            with Database.session() as db:
                entity = db.get(ItemMisc, entity_id)
                if entity is None:
                    return err(NotFoundError(
                        message="ItemMisc not found",
                        entity="ItemMisc",
                        identifier=entity_id,
                    ))
                db.delete(entity)
                db.commit()
                return ok(None)
        except Exception as exc:
            return err(IOError_(
                message="Failed to delete ItemMisc",
                target=str(exc),
            ))


class InventoryRepository(BaseRepository[Inventory]):
    model = Inventory

    @classmethod
    def get_by_character(cls, character_id: int) -> Result[Inventory, NotFoundError | IOError_]:
        """Fetch the inventory for a given character."""
        try:
            with Database.session() as db:
                from sqlalchemy.orm import joinedload
                entity = (
                    db.query(Inventory)
                    .options(joinedload(Inventory.items))
                    .filter(Inventory.character_id == character_id)
                    .first()
                )
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
        """Return all items inside an inventory."""
        try:
            with Database.session() as db:
                entities = (
                    db.query(InventoryItem)
                    .filter(InventoryItem.inventory_id == inventory_id)
                    .all()
                )
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list InventoryItems",
                target=str(exc),
            ))
