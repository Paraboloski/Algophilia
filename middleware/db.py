from __future__ import annotations

from sqlmodel import SQLModel
from typing import AsyncGenerator
from middleware.config import get_env
from contextlib import asynccontextmanager
from middleware.config.core.env import get_env_bool
from middleware.config import ok, err, Result, IOError_
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

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
    async def get_async_session(cls) -> AsyncGenerator[AsyncSession, None]:
        async with cls.SessionLocal() as db:
            try:
                yield db
            except Exception:
                await db.rollback()
                raise

    @classmethod
    async def init_db(cls) -> Result[None, IOError_]:
        try:
            async with cls.engine.begin() as conn: await conn.run_sync(SQLModel.metadata.create_all)
            return ok(None)
        except Exception as e:
            return err(IOError_(
                message="DB init Fail",
                target=str(e),
            ))