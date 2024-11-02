# src/models/roadmap.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    # Relationships
    project = relationship("Project", back_populates="roadmaps")
