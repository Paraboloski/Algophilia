from __future__ import annotations

from typing import Any, Dict
from dataclasses import dataclass

@dataclass(frozen=True, kw_only=True)
class AppError:
    message: str
    code: str | None = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.__class__.__name__,
            "message": self.message,
            "code": self.code,
            "details": self._details(),
        }

    def __str__(self) -> str:
        return str(self.to_dict())

    def _details(self) -> Dict[str, Any]:
        return {}


@dataclass(frozen=True)
class ValidationError(AppError):
    field: str
    value: Any = None

    def _details(self) -> Dict[str, Any]:
        return {
            "field": self.field,
            "value": self.value,
        }


@dataclass(frozen=True)
class ParseError(AppError):
    type: str
    default: str

    def _details(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "default": self.default,
        }


@dataclass(frozen=True)
class IOError_(AppError):
    target: str

    def _details(self) -> Dict[str, Any]:
        return {"target": self.target}


@dataclass(frozen=True)
class NetworkError(AppError):
    url: str
    status: int | None = None

    def _details(self) -> Dict[str, Any]:
        return {
            "url": self.url,
            "status": self.status,
        }


@dataclass(frozen=True)
class NotFoundError(AppError):
    entity: str
    identifier: Any

    def _details(self) -> Dict[str, Any]:
        return {
            "entity": self.entity,
            "identifier": self.identifier,
        }


@dataclass(frozen=True)
class PermissionError_(AppError):
    actor: str
    action: str

    def _details(self) -> Dict[str, Any]:
        return {
            "actor": self.actor,
            "action": self.action,
        }


@dataclass(frozen=True)
class ConflictError(AppError):
    entity: str
    identifier: Any

    def _details(self) -> Dict[str, Any]:
        return {
            "entity": self.entity,
            "identifier": self.identifier,
        }


@dataclass(frozen=True)
class BusinessRuleError(AppError):
    rule: str

    def _details(self) -> Dict[str, Any]:
        return {"rule": self.rule}
