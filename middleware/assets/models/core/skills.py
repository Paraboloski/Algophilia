import enum
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import CheckConstraint, Enum, String, Text, Column

class SkillType(enum.Enum):
    feat = "Feat"
    spell = "Spell"

class God(enum.Enum):
    HASTUR = "HASTUR"
    MARDUK = "MARDUK"
    SULFUR = "SULFUR"
    NEW_GODS = "NEW GODS"
    GORGOROTH = "GORGOROTH"

class Enhanced(SQLModel, table=True):
    __tablename__ = "enhanced"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))

    spells: list["SkillSpell"] = Relationship(back_populates="enhanced_effect")

class Skill(SQLModel, table=True):
    __tablename__ = "skill"

    id: int | None = Field(default=None, primary_key=True)
    description: str | None = Field(default=None, sa_column=Column(Text))
    label: str = Field(sa_column=Column(String(100)))
    type: SkillType = Field(sa_column=Column(Enum(SkillType)))

    feat: "SkillFeat" = Relationship(back_populates="skill", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})
    spell: "SkillSpell" = Relationship(back_populates="skill", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})

class SkillFeat(SQLModel, table=True):
    __tablename__ = "skill_feat"

    skill_id: int = Field(foreign_key="skill.id", ondelete="CASCADE", primary_key=True)

    skill: "Skill" = Relationship(back_populates="feat")

class SkillSpell(SQLModel, table=True):
    __tablename__ = "skill_spell"
    __table_args__ = (
        CheckConstraint("affinity_level >= 0", name="ck_skill_spell_affinity_level"),
    )

    affinity_level: int | None = Field(default=None)
    affinity_with: God = Field(sa_column=Column(Enum(God)))

    skill_id: int = Field(foreign_key="skill.id", ondelete="CASCADE", primary_key=True)
    enhanced_effect_id: int | None = Field(default=None, foreign_key="enhanced.id", ondelete="SET NULL")

    skill: "Skill" = Relationship(back_populates="spell")
    enhanced_effect: "Enhanced | None" = Relationship(back_populates="spells")
