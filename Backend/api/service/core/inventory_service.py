from typing import Sequence
from Backend.api.models.core.items import Inventory, InventoryItem
from Backend.middleware import Result, IOError_, NotFoundError, ok, err
from Backend.api.data.repository import InventoryRepository, InventoryItemRepository, ItemRepository

class InventoryService:
    @classmethod
    def get_inventory(cls, character_id: int) -> Result[Inventory, NotFoundError | IOError_]:
        return InventoryRepository.get_by_character(character_id)

    @classmethod
    def get_inventory_items(cls, inventory_id: int) -> Result[Sequence[InventoryItem], IOError_]:
        return InventoryItemRepository.get_by_inventory(inventory_id)

    @classmethod
    def add_item(cls, inventory_id: int, item_id: int, quantity: int = 1) -> Result[InventoryItem, IOError_ | NotFoundError]:
        if quantity <= 0: return err(IOError_(message="Quantity to add must be greater than 0", target="quantity"))

        item_check = ItemRepository.get_by_id(item_id)
        if item_check.is_err(): return item_check # type: ignore

        items_res = InventoryItemRepository.get_by_inventory(inventory_id)
        if items_res.is_err(): return items_res # type: ignore

        items = items_res.unwrap()
        for idx_item in items:
            if idx_item.item_id == item_id:
                new_quantity = idx_item.quantity + quantity
                return InventoryItemRepository.update(idx_item.id, {"quantity": new_quantity})

        return InventoryItemRepository.create(InventoryItem(inventory_id=inventory_id, item_id=item_id, quantity=quantity, equipped=False))

    @classmethod
    def remove_item(cls, inventory_id: int, item_id: int, quantity: int = 1) -> Result[None, IOError_ | NotFoundError]:
        if quantity <= 0: return err(IOError_(message="Quantity to remove must be greater than 0", target="quantity"))

        items_res = InventoryItemRepository.get_by_inventory(inventory_id)
        if items_res.is_err(): return items_res # type: ignore
        
        items = items_res.unwrap()
        for idx_item in items:
            if idx_item.item_id == item_id:
                if idx_item.quantity <= quantity:
                    return InventoryItemRepository.delete(idx_item.id)
                else:
                    update_res = InventoryItemRepository.update(idx_item.id, {"quantity": idx_item.quantity - quantity})
                    if update_res.is_err(): return update_res # type: ignore
                    return ok(None)

        return err(NotFoundError(message="Item not found in inventory", entity="InventoryItem", identifier=item_id))

    @classmethod
    def equip_item(cls, inventory_item_id: int, equip: bool = True) -> Result[InventoryItem, IOError_ | NotFoundError]:
        return InventoryItemRepository.update(inventory_item_id, {"equipped": equip})
