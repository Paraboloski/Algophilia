from Backend.data import Database
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Trait(Database.Base):
    __tablename__ = "trait"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    souls: Mapped[list["Soul"]] = relationship(back_populates="trait")


class Soul(Database.Base):
    __tablename__ = "soul"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    soul_trait_id: Mapped[int | None] = mapped_column(
        "soul_trait", ForeignKey("trait.id", ondelete="SET NULL"))

    trait: Mapped[Trait | None] = relationship(back_populates="souls")
