from sqlmodel import SQLModel, Field
from sqlalchemy import String, Text, Column

class Condition(SQLModel, table=True):
    __tablename__ = "condition"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))
    is_afflicted: bool = Field(default=False, sa_column_kwargs={"name": "isAfflicted"})
