from result import Result, Ok, Err
from typing import TypeVar, NoReturn, Callable, Coroutine, Any
from src.config.error import AppError

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


def attempt(func: Callable[..., T], error_factory: Callable[[Exception], E], *args, **kwargs) -> Result[T, E]:
    try:
        return Ok(func(*args, **kwargs))
    except Exception as exc:
        return Err(error_factory(exc))


async def attempt_async(coro: Coroutine[Any, Any, T], error_factory: Callable[[Exception], E]) -> Result[T, E]:
    try:
        return Ok(await coro)
    except Exception as exc:
        return Err(error_factory(exc))
