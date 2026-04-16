from Backend.data import Database
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Integer, String, Text


class Condition(Database.Base):
    __tablename__ = "condition"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    is_afflicted: Mapped[bool] = mapped_column(
        "isAfflicted", Boolean, default=False)
