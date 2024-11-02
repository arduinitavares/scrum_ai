# src/models/user_story.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class UserStory(Base):
    __tablename__ = "user_stories"

    id = Column(Integer, primary_key=True, index=True)
    epic_id = Column(Integer, ForeignKey("epics.id"), nullable=False)
    description = Column(String)
    acceptance_criteria = Column(String)
    status = Column(String)
    estimate = Column(Integer)
    value = Column(String)

    # Relationships
    epic = relationship("Epic", back_populates="user_stories")
    tasks = relationship("Task", back_populates="user_story")  # Ensure this matches "user_story" in Task
