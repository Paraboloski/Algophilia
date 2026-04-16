import enum
from Backend.data import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, Enum, ForeignKey, String, Text


class SkillType(enum.Enum):
    feat = "Feat"
    spell = "Spell"


class God(enum.Enum):
    pass


class Enhanced(Base):
    __tablename__ = "enhanced"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100))

    spells: Mapped[list["SkillSpell"]] = relationship(back_populates="enhanced_effect")


class Skill(Base):
    __tablename__ = "skill"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    description: Mapped[str | None] = mapped_column(Text)

    label: Mapped[str] = mapped_column(String(100))

    type: Mapped[SkillType] = mapped_column(Enum(SkillType))

    feat: Mapped["SkillFeat"] = relationship(back_populates="skill", uselist=False, cascade="all, delete-orphan")
    
    spell: Mapped["SkillSpell"] = relationship(back_populates="skill", uselist=False, cascade="all, delete-orphan")


class SkillFeat(Base):
    __tablename__ = "skill_feat"

    skill_id: Mapped[int] = mapped_column(ForeignKey("skill.id", ondelete="CASCADE"), primary_key=True)

    skill: Mapped["Skill"] = relationship(back_populates="feat")


class SkillSpell(Base):
    __tablename__ = "skill_spell"
    __table_args__ = (
        CheckConstraint("affinity_level >= 0", name="ck_skill_spell_affinity_level"),
    )

    affinity_level: Mapped[int | None] = mapped_column()

    affinity_with: Mapped[God] = mapped_column(Enum(God))

    skill: Mapped["Skill"] = relationship(back_populates="spell")

    skill_id: Mapped[int] = mapped_column(ForeignKey("skill.id", ondelete="CASCADE"), primary_key=True)

    enhanced_effect_id: Mapped[int | None] = mapped_column(ForeignKey("enhanced.id", ondelete="SET NULL"))

    enhanced_effect: Mapped["Enhanced | None"] = relationship(back_populates="spells")
