from typing import Any
from sqlalchemy import JSON
from pydantic import BaseModel
from sqlalchemy.engine import Dialect
from sqlalchemy.types import TypeDecorator
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class PydanticType(TypeDecorator):
    impl = JSON

    def __init__(self, pydantic_class):
        super().__init__()
        self.pydantic_class = pydantic_class

    def process_bind_param(self, value: BaseModel | None, dialect: Dialect) -> dict[str, Any] | None:
        return value.model_dump(mode="json") if value else None

    def process_result_value(self, value: dict[str, Any] | None, dialect: Dialect) -> BaseModel | None:
        return self.pydantic_class.model_validate(value) if value else None
