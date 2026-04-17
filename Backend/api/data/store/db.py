from __future__ import annotations

from typing import Generator
from Backend.middleware import get_env
from sqlalchemy import create_engine
from contextlib import contextmanager
from Backend.middleware import ok, err, Result, IOError_
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session


class Base(DeclarativeBase):
    pass


class Database:
    DB_URL = get_env("DATABASE_URL").unwrap()

    engine = create_engine(
        DB_URL,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
        echo=True,
    )

    SessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )

    @classmethod
    @contextmanager
    def session(cls) -> Generator[Session, None, None]:
        db = cls.SessionLocal()
        try:
            yield db
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    @classmethod
    def init_db(cls) -> Result[None, IOError_]:
        try:
            Base.metadata.create_all(bind=cls.engine)
            return ok(None)
        except Exception as e:
            return err(IOError_(
                message="DB init Fail",
                target=str(e),
            ))