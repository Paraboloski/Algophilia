import enum
from typing import Any, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import CheckConstraint, Enum, String, Text, UniqueConstraint, Column, ForeignKey

if TYPE_CHECKING:
    from .characters import Character

class DamageType(enum.Enum):
    pass

class WeaponType(enum.Enum):
    pass

class ItemCategory(enum.Enum):
    pass

class Item(SQLModel, table=True):
    __tablename__: Any = "item"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))
    category: ItemCategory = Field(sa_column=Column(Enum(ItemCategory)))

    artillery: "ItemArtillery" = Relationship(back_populates="item", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})
    armor: "ItemArmor" = Relationship(back_populates="item", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})
    misc: "ItemMisc" = Relationship(back_populates="item", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})

class ItemArtillery(SQLModel, table=True):
    __tablename__: Any = "item_artiglieria"
    __table_args__ = (
        CheckConstraint("dice_count > 0", name="ck_item_artiglieria_dice_count"),
        CheckConstraint("dice_faces > 0", name="ck_item_artiglieria_dice_faces"),
    )

    item_id: int = Field(sa_column=Column(ForeignKey("item.id", ondelete="CASCADE"), primary_key=True))
    bonus_tpc: int = Field(default=0)
    dice_count: int = Field()
    dice_faces: int = Field()
    damage_type: DamageType = Field(sa_column=Column(Enum(DamageType)))
    weapon_type: WeaponType = Field(sa_column=Column(Enum(WeaponType)))
    scaling_stat_id: int | None = Field(
        default=None,
        sa_column=Column(ForeignKey("stat.id", ondelete="SET NULL"), nullable=True),
    )

    item: "Item" = Relationship(back_populates="artillery")

class ItemArmor(SQLModel, table=True):
    __tablename__: Any = "item_armor"
    __table_args__ = (
        CheckConstraint("bonus_ca >= 0", name="ck_item_armor_bonus_ca"),
    )

    item_id: int = Field(sa_column=Column(ForeignKey("item.id", ondelete="CASCADE"), primary_key=True))
    bonus_ca: int = Field()
    penalty: str | None = Field(default=None, sa_column=Column(Text))

    item: "Item" = Relationship(back_populates="armor")

class ItemMisc(SQLModel, table=True):
    __tablename__: Any = "item_misc"

    item_id: int = Field(sa_column=Column(ForeignKey("item.id", ondelete="CASCADE"), primary_key=True))

    item: "Item" = Relationship(back_populates="misc")

class Inventory(SQLModel, table=True):
    __tablename__: Any = "inventory"

    id: int | None = Field(default=None, primary_key=True)
    character_id: int = Field(sa_column=Column(ForeignKey("character.id", ondelete="CASCADE"), unique=True))

    character: "Character" = Relationship(back_populates="inventory")
    items: list["InventoryItem"] = Relationship(back_populates="inventory", sa_relationship_kwargs={"cascade": "all, delete-orphan"})

class InventoryItem(SQLModel, table=True):
    __tablename__: Any = "inventory_item"
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="ck_inventory_item_quantity"),
        UniqueConstraint("inventory_id", "item_id", name="unique_inventory_item"),
    )

    id: int | None = Field(default=None, primary_key=True)
    inventory_id: int = Field(sa_column=Column(ForeignKey("inventory.id", ondelete="CASCADE")))
    item_id: int = Field(sa_column=Column(ForeignKey("item.id", ondelete="CASCADE")))
    quantity: int = Field(default=1)
    equipped: bool = Field(default=False)

    inventory: "Inventory" = Relationship(back_populates="items")
