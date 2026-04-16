import enum
from .characters import Character
from Backend.data import Database
from sqlalchemy import Boolean, CheckConstraint, Enum, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


class DamageType(enum.Enum):
    pass


class WeaponType(enum.Enum):
    pass


class ItemCategory(enum.Enum):
    pass


class Item(Database.Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    label: Mapped[str] = mapped_column(String(100), nullable=False)

    description: Mapped[str | None] = mapped_column(Text)

    category: Mapped[ItemCategory] = mapped_column(
        Enum(ItemCategory), nullable=False)

    artillery: Mapped["ItemArtillery"] = relationship(
        back_populates="item", uselist=False, cascade="all, delete-orphan")

    armor: Mapped["ItemArmor"] = relationship(
        back_populates="item", uselist=False, cascade="all, delete-orphan")

    misc: Mapped["ItemMisc"] = relationship(
        back_populates="item", uselist=False, cascade="all, delete-orphan")


class ItemArtillery(Database.Base):
    __tablename__ = "item_artiglieria"
    __table_args__ = (
        CheckConstraint("dice_count > 0",
                        name="ck_item_artiglieria_dice_count"),
        CheckConstraint("dice_faces > 0",
                        name="ck_item_artiglieria_dice_faces"),
    )

    item_id: Mapped[int] = mapped_column(ForeignKey(
        "item.id", ondelete="CASCADE"), primary_key=True)

    bonus_tpc: Mapped[int] = mapped_column(Integer, default=0)

    dice_count: Mapped[int] = mapped_column(Integer, nullable=False)

    dice_faces: Mapped[int] = mapped_column(Integer, nullable=False)

    damage_type: Mapped[DamageType] = mapped_column(
        Enum(DamageType), nullable=False)

    weapon_type: Mapped[WeaponType] = mapped_column(
        Enum(WeaponType), nullable=False)

    scaling_stat_id: Mapped[int | None] = mapped_column(
        ForeignKey("stat.id", ondelete="SET NULL"))

    item: Mapped["Item"] = relationship(back_populates="artillery")


class ItemArmor(Database.Base):
    __tablename__ = "item_armor"
    __table_args__ = (
        CheckConstraint("bonus_ca >= 0", name="ck_item_armor_bonus_ca"),
    )

    item_id: Mapped[int] = mapped_column(ForeignKey(
        "item.id", ondelete="CASCADE"), primary_key=True)

    bonus_ca: Mapped[int] = mapped_column(Integer, nullable=False)

    item: Mapped["Item"] = relationship(back_populates="armor")


class ItemMisc(Database.Base):
    __tablename__ = "item_misc"

    item_id: Mapped[int] = mapped_column(ForeignKey(
        "item.id", ondelete="CASCADE"), primary_key=True)

    item: Mapped["Item"] = relationship(back_populates="misc")


class Inventory(Database.Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    character_id: Mapped[int] = mapped_column(ForeignKey(
        "character.id", ondelete="CASCADE"), nullable=False, unique=True)

    character: Mapped["Character"] = relationship(back_populates="inventory")

    items: Mapped[list["InventoryItem"]] = relationship(
        back_populates="inventory", cascade="all, delete-orphan")


class InventoryItem(Database.Base):
    __tablename__ = "inventory_item"
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="ck_inventory_item_quantity"),
        UniqueConstraint("inventory_id", "item_id",
                         name="unique_inventory_item"),
    )

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    inventory_id: Mapped[int] = mapped_column(ForeignKey(
        "inventory.id", ondelete="CASCADE"), nullable=False)

    item_id: Mapped[int] = mapped_column(ForeignKey(
        "item.id", ondelete="CASCADE"), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    equipped: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)

    inventory: Mapped["Inventory"] = relationship(back_populates="items")
