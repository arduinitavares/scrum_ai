# src/models/example.py
from sqlalchemy import Column, Integer, String
from src.db.session import Base

class Example(Base):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
