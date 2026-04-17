import enum
from typing import Any
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import CheckConstraint, Enum, String, Column, ForeignKey

class StatType(enum.Enum):
    attribute = "attribute"
    resource = "resource"
    progress = "progress"

class Stat(SQLModel, table=True):
    __tablename__: Any = "stat"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    type: StatType = Field(sa_column=Column(Enum(StatType)))

    resource: "StatResource" = Relationship(back_populates="stat", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})
    progress: "StatProgress" = Relationship(back_populates="stat", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})
    attribute: "StatAttribute" = Relationship(back_populates="stat", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})

class StatAttribute(SQLModel, table=True):
    __tablename__: Any = "stat_attribute"
    __table_args__ = (
        CheckConstraint("value >= 0 AND value < 999", name="ck_stat_attribute_value"),
    )

    stat_id: int = Field(sa_column=Column(ForeignKey("stat.id", ondelete="CASCADE"), primary_key=True))
    value: int = Field()
    color: str | None = Field(default=None)

    stat: "Stat" = Relationship(back_populates="attribute")

class StatResource(SQLModel, table=True):
    __tablename__: Any = "stat_resource"
    __table_args__ = (
        CheckConstraint("max_value >= 0", name="ck_stat_resource_max_value"),
        CheckConstraint("current_value >= 0 AND current_value < 999", name="ck_stat_resource_current_value"),
        CheckConstraint("current_value <= max_value", name="ck_stat_resource_current_le_max"),
    )

    stat_id: int = Field(sa_column=Column(ForeignKey("stat.id", ondelete="CASCADE"), primary_key=True))
    max_value: int = Field()
    current_value: int = Field()

    stat: "Stat" = Relationship(back_populates="resource")

class StatProgress(SQLModel, table=True):
    __tablename__: Any = "stat_progress"
    __table_args__ = (
        CheckConstraint("max_steps > 0", name="ck_stat_progress_max_steps"),
        CheckConstraint("current_step >= 0", name="ck_stat_progress_current_step"),
        CheckConstraint("current_step <= max_steps", name="ck_stat_progress_current_le_max"),
    )

    stat_id: int = Field(sa_column=Column(ForeignKey("stat.id", ondelete="CASCADE"), primary_key=True))
    max_steps: int = Field()
    current_step: int = Field()

    stat: "Stat" = Relationship(back_populates="progress")
