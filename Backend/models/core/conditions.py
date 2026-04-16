from Backend.data import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Condition(Base):
    __tablename__ = "condition"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100))

    is_afflicted: Mapped[bool] = mapped_column("isAfflicted", default=False)
