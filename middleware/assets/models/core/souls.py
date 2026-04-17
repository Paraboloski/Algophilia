from typing import Any
from sqlalchemy import String, Text, Column, ForeignKey
from sqlmodel import SQLModel, Field, Relationship

class Trait(SQLModel, table=True):
    __tablename__: Any = "trait"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))

    souls: list["Soul"] = Relationship(back_populates="trait")

class Soul(SQLModel, table=True):
    __tablename__: Any = "soul"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))
    soul_trait_id: int | None = Field(
        default=None,
        sa_column=Column("soul_trait", ForeignKey("trait.id", ondelete="SET NULL"), nullable=True),
    )

    trait: Trait | None = Relationship(back_populates="souls")
