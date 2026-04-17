from __future__ import annotations

import os
from result import Result
from typing import Callable, TypeVar
from dotenv import load_dotenv, find_dotenv
from middleware.config.core.options import err, ok
from middleware.config.core.error import AppError, ParseError, ValidationError

load_dotenv(find_dotenv())

T = TypeVar("T")

def _safe_cast(key: str, raw: str, cast: Callable[[str], T], type: str) -> Result[T, AppError]:
    try:
        return ok(cast(raw))
    except Exception:
        return err(ParseError(
            message=f"Environment variable '{key}' could not be parsed as {type}",
            default=raw,
            type=type,
        ))


def get_env(key: str) -> Result[str, AppError]:
    value = os.getenv(key)
    if not value:
        return err(ValidationError(
            message=f"Environment variable '{key}' is not set or empty",
            field=key,
            value=value,
        ))
    return ok(value)


def get_env_or(key: str, default: str) -> str:
    return get_env(key).unwrap_or(default)


def get_env_as(key: str, cast: Callable[[str], T], type: str) -> Result[T, AppError]:
    return get_env(key).and_then(lambda raw: _safe_cast(key, raw, cast, type))


def get_env_int(key: str) -> Result[int, AppError]:
    return get_env_as(key, int, "int")


def get_env_float(key: str) -> Result[float, AppError]:
    return get_env_as(key, float, "float")


def get_env_bool(key: str) -> Result[bool, AppError]:
    TRUE = {"true", "1", "yes"}
    FALSE = {"false", "0", "no"}

    def parse(raw: str) -> bool:
        val = raw.strip().lower()
        if val in TRUE:
            return True
        if val in FALSE:
            return False
        raise ValueError(f"Cannot parse {raw!r} as bool")

    return get_env_as(key, parse, "bool")
