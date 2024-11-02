# src/models/task.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_story_id = Column(Integer, ForeignKey("user_stories.id"), nullable=False)
    sprint_id = Column(Integer, ForeignKey("sprints.id"))
    description = Column(String)
    status = Column(String)
    estimate = Column(Integer)
    type = Column(String)

    # Relationships
    user_story = relationship("UserStory", back_populates="tasks")  # Ensure this matches "tasks" in UserStory
    sprint = relationship("Sprint", back_populates="tasks")
