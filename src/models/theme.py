# src/models/theme.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    order = Column(Integer)

    # Relationships
    project = relationship("Project", back_populates="themes")
    features = relationship("Feature", back_populates="theme")
