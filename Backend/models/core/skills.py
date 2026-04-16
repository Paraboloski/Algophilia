import enum
from Backend.data import Database
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, Enum, ForeignKey, Integer, String, Text


class SkillType(enum.Enum):
    feat = "Feat"
    spell = "Spell"


class God(enum.Enum):
    pass


class Enhanced(Database.Base):
    __tablename__ = "enhanced"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    spells: Mapped[list["SkillSpell"]] = relationship(
        back_populates="enhanced_effect")


class Skill(Database.Base):
    __tablename__ = "skill"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100), nullable=False)

    type: Mapped[SkillType] = mapped_column(Enum(SkillType), nullable=False)

    Feat: Mapped["SkillFeat"] = relationship(
        back_populates="skill", uselist=False, cascade="all, delete-orphan")
    Spell: Mapped["SkillSpell"] = relationship(
        back_populates="skill", uselist=False, cascade="all, delete-orphan")


class SkillFeat(Database.Base):
    __tablename__ = "skill_feat"

    skill_id: Mapped[int] = mapped_column(ForeignKey(
        "skill.id", ondelete="CASCADE"), primary_key=True)

    skill: Mapped["Skill"] = relationship(back_populates="feat")


class SkillSpell(Database.Base):
    __tablename__ = "skill_spell"
    __table_args__ = (
        CheckConstraint("affinity_level >= 0",
                        name="ck_skill_spell_affinity_level"),
    )

    affinity_level: Mapped[int | None] = mapped_column(Integer)

    affinity_with: Mapped[God] = mapped_column(Enum(God), nullable=False)

    skill: Mapped["Skill"] = relationship(back_populates="spell")

    skill_id: Mapped[int] = mapped_column(ForeignKey(
        "skill.id", ondelete="CASCADE"), primary_key=True)

    enhanced_effect_id: Mapped[int | None] = mapped_column(
        ForeignKey("enhanced.id", ondelete="SET NULL"))

    enhanced_effect: Mapped["Enhanced | None"] = relationship(
        back_populates="spells")
