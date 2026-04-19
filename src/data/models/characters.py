from typing import Any, TYPE_CHECKING
from sqlalchemy import String, Text, Column, ForeignKey
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .stats import Stat
    from .souls import Soul
    from .skills import Skill
    from .origins import Origin
    from .items import Inventory
    from .knowledges import Knowledge
    from .conditions import Condition

class Character(SQLModel, table=True):
    __tablename__: Any = "character"

    id: int | None = Field(default=None, primary_key=True)
    level: int = Field()
    name: str = Field(sa_column=Column(String(100)))
    notes: str | None = Field(default=None, sa_column=Column(Text))
    backstory: str | None = Field(default=None, sa_column=Column(Text))

    soul_id: int | None = Field(default=None, sa_column=Column(ForeignKey("soul.id", ondelete="SET NULL"), nullable=True))
    origin_id: int | None = Field(default=None, sa_column=Column(ForeignKey("origin.id", ondelete="SET NULL"), nullable=True))

    soul: "Soul" = Relationship(sa_relationship_kwargs={"foreign_keys": "[Character.soul_id]"})
    origin: "Origin" = Relationship(sa_relationship_kwargs={"foreign_keys": "[Character.origin_id]"})
    
    inventory: "Inventory" = Relationship(back_populates="character", sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"})

    stats: list["CharacterStat"] = Relationship(back_populates="character", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    skills: list["CharacterSkill"] = Relationship(back_populates="character", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    conditions: list["CharacterCondition"] = Relationship(back_populates="character", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    knowledges: list["CharacterKnowledge"] = Relationship(back_populates="character", sa_relationship_kwargs={"cascade": "all, delete-orphan"})

class CharacterStat(SQLModel, table=True):
    __tablename__: Any = "character_stat"

    character_id: int = Field(sa_column=Column(ForeignKey("character.id", ondelete="CASCADE"), primary_key=True))
    stat_id: int = Field(sa_column=Column(ForeignKey("stat.id", ondelete="CASCADE"), primary_key=True))

    character: "Character" = Relationship(back_populates="stats")
    stat: "Stat" = Relationship()

class CharacterCondition(SQLModel, table=True):
    __tablename__: Any = "character_condition"

    character_id: int = Field(sa_column=Column(ForeignKey("character.id", ondelete="CASCADE"), primary_key=True))
    condition_id: int = Field(sa_column=Column(ForeignKey("condition.id", ondelete="CASCADE"), primary_key=True))

    character: "Character" = Relationship(back_populates="conditions")
    condition: "Condition" = Relationship()

class CharacterKnowledge(SQLModel, table=True):
    __tablename__: Any = "character_knowledge"

    character_id: int = Field(sa_column=Column(ForeignKey("character.id", ondelete="CASCADE"), primary_key=True))
    knowledge_id: int = Field(sa_column=Column(ForeignKey("knowledge.id", ondelete="CASCADE"), primary_key=True))
    is_proficient: bool = Field(default=False)

    character: "Character" = Relationship(back_populates="knowledges")
    knowledge: "Knowledge" = Relationship()

class CharacterSkill(SQLModel, table=True):
    __tablename__: Any = "character_skill"

    character_id: int = Field(sa_column=Column(ForeignKey("character.id", ondelete="CASCADE"), primary_key=True))
    skill_id: int = Field(sa_column=Column(ForeignKey("skill.id", ondelete="CASCADE"), primary_key=True))

    character: "Character" = Relationship(back_populates="skills")
    skill: "Skill" = Relationship()
