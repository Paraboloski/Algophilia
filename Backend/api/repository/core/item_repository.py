from typing import Sequence
from sqlalchemy import select
from middleware.db import Database
from middleware.config import Result, ok, err, IOError_, NotFoundError
from Backend.api.repository.core.base import BaseRepository, eager_joinedload, sql_eq
from middleware.assets.models.core.items import Item, ItemArtillery, ItemArmor, ItemMisc, Inventory, InventoryItem

class ItemArtilleryRepository(BaseRepository[ItemArtillery]):
    model = ItemArtillery


class ItemArmorRepository(BaseRepository[ItemArmor]):
    model = ItemArmor


class ItemMiscRepository(BaseRepository[ItemMisc]):
    model = ItemMisc


class InventoryRepository(BaseRepository[Inventory]):
    model = Inventory

    @classmethod
    async def get_by_character(cls, character_id: int) -> Result[Inventory, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Inventory)
                    .options(eager_joinedload(Inventory.items))
                    .where(sql_eq(Inventory.character_id, character_id))
                )
                entity = result.scalars().unique().first()
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


class ItemRepository(BaseRepository[Item]):
    model = Item

    @classmethod
    async def get_with_details(cls, entity_id: int) -> Result[Item, NotFoundError | IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Item)
                    .options(
                        eager_joinedload(Item.artillery),
                        eager_joinedload(Item.armor),
                        eager_joinedload(Item.misc),
                    )
                    .where(sql_eq(Item.id, entity_id))
                )
                entity = result.scalars().unique().first()
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
    async def get_by_category(cls, category) -> Result[Sequence[Item], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(Item).where(sql_eq(Item.category, category))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to fetch Items by category",
                target=str(exc),
            ))


class InventoryItemRepository(BaseRepository[InventoryItem]):
    model = InventoryItem

    @classmethod
    async def get_by_inventory(cls, inventory_id: int) -> Result[Sequence[InventoryItem], IOError_]:
        try:
            async with Database.get_async_session() as db:
                result = await db.execute(
                    select(InventoryItem)
                    .where(sql_eq(InventoryItem.inventory_id, inventory_id))
                )
                entities = result.scalars().all()
                for e in entities:
                    db.expunge(e)
                return ok(entities)
        except Exception as exc:
            return err(IOError_(
                message="Failed to list InventoryItems",
                target=str(exc),
            ))
