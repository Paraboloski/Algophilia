from Backend.api.data import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Knowledge(Base):
    __tablename__ = "knowledge"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100))

    is_proficient: Mapped[bool] = mapped_column("isProficient", default=False)
