from __future__ import annotations

from result import Result
from sqlmodel import SQLModel
from contextlib import asynccontextmanager 
from typing import TypeVar, Any, AsyncGenerator, Callable, Coroutine
from src.config import IOError_, get_env, get_env_bool, attempt_async
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

T = TypeVar("T")

class Database:
    DB_URL = get_env("DATABASE_URL").unwrap().replace("sqlite:///", "sqlite+aiosqlite:///")
    IS_DEV = get_env_bool("IS_DEV").unwrap_or(False)

    engine = create_async_engine(
        DB_URL,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
        echo=IS_DEV,
    )

    SessionLocal = async_sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )

    @classmethod
    @asynccontextmanager
    async def _get_async_session(cls) -> AsyncGenerator[AsyncSession, None]:
        async with cls.SessionLocal() as db:
            try:
                yield db
            except Exception:
                await db.rollback()
                raise

    @classmethod
    async def session_scope(cls, func: Callable[[AsyncSession], Coroutine[Any, Any, T]]) -> Result[T, IOError_]:
        async def _run():
            async with cls._get_async_session() as db:
                return await func(db)

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="Database session error", target=str(e))
        )

    @classmethod
    async def init_db(cls) -> Result[None, IOError_]:
        async def _run():
            async with cls.engine.begin() as conn:
                await conn.run_sync(SQLModel.metadata.create_all)

        return await attempt_async(
            _run(),
            lambda e: IOError_(message="DB init Fail", target=str(e))
        )