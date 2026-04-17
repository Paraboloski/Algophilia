from Backend.api.data import Base
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Trait(Base):
    __tablename__ = "trait"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100))

    souls: Mapped[list["Soul"]] = relationship(back_populates="trait")


class Soul(Base):
    __tablename__ = "soul"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100))

    soul_trait_id: Mapped[int | None] = mapped_column("soul_trait", ForeignKey("trait.id", ondelete="SET NULL"))

    trait: Mapped[Trait | None] = relationship(back_populates="souls")
