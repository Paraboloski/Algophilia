from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import String, Text, Column

class OriginKnowledge(SQLModel, table=True):
    __tablename__ = "origin_knowledge"

    origin_id: int = Field(foreign_key="origin.id", ondelete="CASCADE", primary_key=True)
    knowledge_id: int = Field(foreign_key="knowledge.id", ondelete="CASCADE", primary_key=True)

    origin: "Origin" = Relationship(back_populates="knowledges")

class Origin(SQLModel, table=True):
    __tablename__ = "origin"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))

    knowledges: list["OriginKnowledge"] = Relationship(back_populates="origin", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
