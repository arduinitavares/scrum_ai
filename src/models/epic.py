# src/models/epic.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class Epic(Base):
    __tablename__ = "epics"

    id = Column(Integer, primary_key=True, index=True)
    feature_id = Column(Integer, ForeignKey("features.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(String)

    # Relationships
    feature = relationship("Feature", back_populates="epics")
    user_stories = relationship("UserStory", back_populates="epic")
