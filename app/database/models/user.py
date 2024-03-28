from sqlalchemy import Column, Integer, String
from .base import Base, DB_SCHEMA


class UserBase(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": DB_SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), nullable=False)
    department_description = Column(String(255), nullable=False)
