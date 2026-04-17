from sqlalchemy import String, Text, Column
from sqlmodel import SQLModel, Field, Relationship

class Trait(SQLModel, table=True):
    __tablename__ = "trait"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))

    souls: list["Soul"] = Relationship(back_populates="trait")

class Soul(SQLModel, table=True):
    __tablename__ = "soul"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))
    soul_trait_id: int | None = Field(default=None, foreign_key="trait.id", sa_column_kwargs={"name": "soul_trait", "ondelete": "SET NULL"})

    trait: Trait | None = Relationship(back_populates="souls")
