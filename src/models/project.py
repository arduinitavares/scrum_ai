# src/models/project.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from src.db.session import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)

    # Relationships
    sprints = relationship("Sprint", back_populates="project")
    roadmaps = relationship("Roadmap", back_populates="project")
    visions = relationship("Vision", back_populates="project")
    themes = relationship("Theme", back_populates="project")
