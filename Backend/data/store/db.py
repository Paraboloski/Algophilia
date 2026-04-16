from __future__ import annotations

from typing import Generator
from Backend.config import get_env
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from Backend.config import ok, err, Result, IOError_

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
    
    Base = declarative_base()

    @classmethod
    @contextmanager
    def session(cls) -> Generator[Session, None, None]:
        db = cls.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @classmethod
    def init_db(cls) -> Result[None, IOError_]:
        try:
            cls.Base.metadata.create_all(bind=cls.engine)
            return ok(None)
        except Exception as e:
            return err(IOError_(
                message="DB init Fail",
                target=str(e),
            ))