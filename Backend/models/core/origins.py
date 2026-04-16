from Backend.data import Database
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Origin(Database.Base):
    __tablename__ = "origin"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    knowledges: Mapped[list["OriginKnowledge"]] = relationship(
        back_populates="origin", cascade="all, delete-orphan")


class OriginKnowledge(Database.Base):
    __tablename__ = "origin_knowledge"

    origin_id: Mapped[int] = mapped_column(ForeignKey(
        "origin.id", ondelete="CASCADE"), primary_key=True)
    knowledge_id: Mapped[int] = mapped_column(ForeignKey(
        "knowledge.id", ondelete="CASCADE"), primary_key=True)

    origin: Mapped["Origin"] = relationship(back_populates="knowledges")
