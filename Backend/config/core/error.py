from __future__ import annotations
from typing import Any, TypeVar
from dataclasses import dataclass
from result import Err, Ok, Result

T = TypeVar("T")
E = TypeVar("E", bound="AppError")


@dataclass(frozen=True)
class AppError:
    message: str

    def __str__(self) -> str:
        details = self._details()
        detail_part = f" {details}" if details else ""
        return f"[{self.__class__.__name__}]{detail_part} — {self.message}"

    def _details(self) -> str:
        return ""


@dataclass(frozen=True)
class ValidationError(AppError):
    field: str
    value: Any = None

    def _details(self) -> str:
        return f"field={self.field!r} value={self.value!r}"


@dataclass(frozen=True)
class ParseError(AppError):
    type: str
    default: str

    def _details(self) -> str:
        return f"default={self.default!r} as {self.type}"


@dataclass(frozen=True)
class IOError_(AppError):
    target: str

    def _details(self) -> str:
        return f"{self.target!r}"


@dataclass(frozen=True)
class NetworkError(AppError):
    url: str
    status: int | None = None

    def _details(self) -> str:
        return f"{self.url!r}" + (f" (HTTP {self.status})" if self.status else "")


@dataclass(frozen=True)
class NotFoundError(AppError):
    entity: str
    identifier: Any

    def _details(self) -> str:
        return f"{self.entity} id={self.identifier!r}"


@dataclass(frozen=True)
class PermissionError_(AppError):
    actor: str
    action: str

    def _details(self) -> str:
        return f"actor={self.actor!r} action={self.action!r}"


@dataclass(frozen=True)
class ConflictError(AppError):
    entity: str
    identifier: Any

    def _details(self) -> str:
        return f"{self.entity} id={self.identifier!r}"


@dataclass(frozen=True)
class BusinessRuleError(AppError):
    rule: str

    def _details(self) -> str:
        return f"rule={self.rule!r}"


def ok(value: T) -> Result[T, Any]:
    return Ok(value)


def err(error: E) -> Result[Any, E]:
    return Err(error)


def guard(condition: bool, error: E) -> Result[None, E]:
    return Ok(None) if condition else Err(error)
