from result import Result, Ok, Err

from Backend.config.core.env import (
    get_env,
    get_env_or,
    get_env_as,
    get_env_int,
    get_env_bool,
    get_env_float,
)

from Backend.config.core.error import (
    IOError_,
    AppError,
    ParseError,
    NetworkError,
    NotFoundError,
    ConflictError,
    ValidationError,
    PermissionError_,
    BusinessRuleError,

    ok,
    err,
    guard,
)

__all__ = [

    "get_env",
    "get_env_or",
    "get_env_as",
    "get_env_int",
    "get_env_bool",
    "get_env_float",

    "IOError_",
    "AppError",
    "ParseError",
    "NetworkError",
    "NotFoundError",
    "ConflictError",
    "ValidationError",
    "PermissionError_",
    "BusinessRuleError",

    "ok",
    "err",
    "guard",
]

__all__ += ["Result", "Ok", "Err"]
