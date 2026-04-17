from .error import AppError
from result import Result, Ok, Err
from typing import TypeVar, NoReturn

T = TypeVar("T")
E = TypeVar("E", bound=AppError)


def ok(value: T) -> Result[T, E]:
    return Ok(value)


def err(error: E) -> Result[NoReturn, E]:
    return Err(error)


def guard(condition: bool, error: E) -> Result[None, E]:
    if not condition:
        return Err(error)
    return Ok(None)
