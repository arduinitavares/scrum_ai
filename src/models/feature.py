# src/models/feature.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(String)

    # Relationships
    theme = relationship("Theme", back_populates="features")
    epics = relationship("Epic", back_populates="feature")
