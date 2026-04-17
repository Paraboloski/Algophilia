from sqlmodel import SQLModel, Field
from sqlalchemy import String, Text, Column

class Knowledge(SQLModel, table=True):
    __tablename__ = "knowledge"

    id: int | None = Field(default=None, primary_key=True)
    label: str = Field(sa_column=Column(String(100)))
    description: str | None = Field(default=None, sa_column=Column(Text))
    is_proficient: bool = Field(default=False, sa_column_kwargs={"name": "isProficient"})
