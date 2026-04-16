import enum
from Backend.data import Database
from sqlalchemy import CheckConstraint, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class StatType(enum.Enum):
    attribute = "attribute"
    resource = "resource"
    progress = "progress"


class Stat(Database.Base):
    __tablename__ = "stat"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    type: Mapped[StatType] = mapped_column(Enum(StatType), nullable=False)

    resource: Mapped["StatResource"] = relationship(
        back_populates="stat", uselist=False, cascade="all, delete-orphan")

    progress: Mapped["StatProgress"] = relationship(
        back_populates="stat", uselist=False, cascade="all, delete-orphan")

    attribute: Mapped["StatAttribute"] = relationship(
        back_populates="stat", uselist=False, cascade="all, delete-orphan")


class StatAttribute(Database.Base):
    __tablename__ = "stat_attribute"
    __table_args__ = (
        CheckConstraint("value >= 0 AND value < 999",
                        name="ck_stat_attribute_value"),
    )

    stat_id: Mapped[int] = mapped_column(ForeignKey(
        "stat.id", ondelete="CASCADE"), primary_key=True)

    value: Mapped[int] = mapped_column(Integer, nullable=False)

    stat: Mapped["Stat"] = relationship(back_populates="attribute")


class StatResource(Database.Base):
    __tablename__ = "stat_resource"
    __table_args__ = (
        CheckConstraint("max_value >= 0", name="ck_stat_resource_max_value"),
        CheckConstraint("current_value >= 0 AND current_value < 999",
                        name="ck_stat_resource_current_value"),
        CheckConstraint("current_value <= max_value",
                        name="ck_stat_resource_current_le_max"),
    )

    stat_id: Mapped[int] = mapped_column(ForeignKey(
        "stat.id", ondelete="CASCADE"), primary_key=True)

    max_value: Mapped[int] = mapped_column(Integer, nullable=False)

    current_value: Mapped[int] = mapped_column(Integer, nullable=False)

    stat: Mapped["Stat"] = relationship(back_populates="resource")


class StatProgress(Database.Base):
    __tablename__ = "stat_progress"
    __table_args__ = (
        CheckConstraint("max_steps > 0", name="ck_stat_progress_max_steps"),
        CheckConstraint("current_step >= 0",
                        name="ck_stat_progress_current_step"),
        CheckConstraint("current_step <= max_steps",
                        name="ck_stat_progress_current_le_max"),
    )

    stat_id: Mapped[int] = mapped_column(ForeignKey(
        "stat.id", ondelete="CASCADE"), primary_key=True)

    max_steps: Mapped[int] = mapped_column(Integer, nullable=False)

    current_step: Mapped[int] = mapped_column(Integer, nullable=False)

    stat: Mapped["Stat"] = relationship(back_populates="progress")
