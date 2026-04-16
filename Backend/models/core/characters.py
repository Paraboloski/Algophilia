from Backend.data import Database
from Backend.models.core.stats import Stat
from Backend.models.core.souls import Soul
from Backend.models.core.skills import Skill
from Backend.models.core.origins import Origin
from Backend.models.core.items import Inventory
from Backend.models.core.knowledges import Knowledge
from Backend.models.core.conditions import Condition
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Character(Database.Base):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    level: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str | None] = mapped_column(Text)
    backstory: Mapped[str | None] = mapped_column(Text)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    soul_id: Mapped[int | None] = mapped_column(
        ForeignKey("soul.id", ondelete="SET NULL"))
    origin_id: Mapped[int | None] = mapped_column(
        ForeignKey("origin.id", ondelete="SET NULL"))

    soul: Mapped["Soul"] = relationship(foreign_keys=[soul_id])
    origin: Mapped["Origin"] = relationship(foreign_keys=[origin_id])
    inventory: Mapped["Inventory"] = relationship(
        back_populates="character", uselist=False, cascade="all, delete-orphan")

    stats: Mapped[list["CharacterStat"]] = relationship(
        back_populates="character", cascade="all, delete-orphan")
    skills: Mapped[list["CharacterSkill"]] = relationship(
        back_populates="character", cascade="all, delete-orphan")
    conditions: Mapped[list["CharacterCondition"]] = relationship(
        back_populates="character", cascade="all, delete-orphan")
    knowledges: Mapped[list["CharacterKnowledge"]] = relationship(
        back_populates="character", cascade="all, delete-orphan")


class CharacterStat(Database.Base):
    __tablename__ = "character_stat"

    character_id: Mapped[int] = mapped_column(ForeignKey(
        "character.id", ondelete="CASCADE"), primary_key=True)
    
    stat_id: Mapped[int] = mapped_column(ForeignKey(
        "stat.id", ondelete="CASCADE"), primary_key=True)

    character: Mapped["Character"] = relationship(back_populates="stats")
    
    stat: Mapped["Stat"] = relationship()


class CharacterCondition(Database.Base):
    __tablename__ = "character_condition"

    character_id: Mapped[int] = mapped_column(ForeignKey(
        "character.id", ondelete="CASCADE"), primary_key=True)
    
    condition_id: Mapped[int] = mapped_column(ForeignKey(
        "condition.id", ondelete="CASCADE"), primary_key=True)

    character: Mapped["Character"] = relationship(back_populates="conditions")
    
    condition: Mapped["Condition"] = relationship()


class CharacterKnowledge(Database.Base):
    __tablename__ = "character_knowledge"

    character_id: Mapped[int] = mapped_column(ForeignKey(
        "character.id", ondelete="CASCADE"), primary_key=True)
    knowledge_id: Mapped[int] = mapped_column(ForeignKey(
        "knowledge.id", ondelete="CASCADE"), primary_key=True)

    is_proficient: Mapped[bool] = mapped_column(
        Integer, default=False, nullable=False)

    character: Mapped["Character"] = relationship(back_populates="knowledges")
    
    knowledge: Mapped["Knowledge"] = relationship()


class CharacterSkill(Database.Base):
    __tablename__ = "character_skill"

    character_id: Mapped[int] = mapped_column(ForeignKey(
        "character.id", ondelete="CASCADE"), primary_key=True)
    
    skill_id: Mapped[int] = mapped_column(ForeignKey(
        "skill.id", ondelete="CASCADE"), primary_key=True)

    character: Mapped["Character"] = relationship(back_populates="skills")
    
    skill: Mapped["Skill"] = relationship()
