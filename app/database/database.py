from datetime import date, datetime
from typing import (
    Annotated,
    Any,
    List,
    Dict,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    Callable,
    cast,
)
import struct
import json
import os

from fastapi import Depends
from sqlalchemy import (
    Date,
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Table,
    MetaData,
    func,
    and_,
)
from sqlalchemy.orm import Session, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from app.database.models.base import DB_SCHEMA

# SQLAlchemy setup
URL_DATABASE = f"mysql+pymysql://root:admin123@localhost:3306/{DB_SCHEMA}"
engine = create_engine(URL_DATABASE, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db_session():
    db = SessionLocal()
    return db


def get_db_engine():
    return engine


def get_db_url():
    return URL_DATABASE


def get_db_session_local():
    return SessionLocal()


def get_db_session_local_engine():
    return engine


def get_db_session_local_url():
    return URL_DATABASE


db_dependency = Annotated[Session, Depends(get_db)]
