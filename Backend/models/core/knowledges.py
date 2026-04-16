from Backend.data import Database
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Integer, String, Text


class Knowledge(Database.Base):
    __tablename__ = "knowledge"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    is_proficient: Mapped[bool] = mapped_column(
        "isProficient", Boolean, default=False)
