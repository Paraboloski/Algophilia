from __future__ import annotations

import os
from result import Result
from typing import Callable, TypeVar
from dotenv import load_dotenv, find_dotenv
from src.config.options import err, ok, attempt
from src.config.error import AppError, ParseError, ValidationError

load_dotenv(find_dotenv())

T = TypeVar("T")

def _safe_cast(key: str, raw: str, cast: Callable[[str], T], type: str) -> Result[T, AppError]:
    return attempt(
        cast,
        lambda _: ParseError(
            message=f"Environment variable '{key}' could not be parsed as {type}",
            default=raw,
            type=type,
        ),
        raw
    )


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
    TRUE = {"true", "1", "yes", "on", "y", "t"}
    FALSE = {"false", "0", "no", "off", "n", "f"}

    def parse(raw: str) -> Result[bool, AppError]:
        val = raw.strip().lower()
        if val in TRUE:
            return ok(True)
        if val in FALSE:
            return ok(False)
        return err(ParseError(
            message=f"Cannot parse {raw!r} as bool",
            default=raw,
            type="bool"
        ))

    return get_env(key).and_then(parse)
