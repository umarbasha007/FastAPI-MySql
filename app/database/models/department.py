from sqlalchemy import Column, Integer, String
from .base import Base, DB_SCHEMA


class DepartmentBase(Base):
    __tablename__ = "department"
    __table_args__ = {"schema": DB_SCHEMA}

    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(50), nullable=False)
    department_description = Column(String(255), nullable=False)
