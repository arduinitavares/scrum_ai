# scripts/test_models.py
from sqlalchemy.orm import Session
from src.db.session import SessionLocal
from src.models.project import Project
from src.models.vision import Vision
from src.models.roadmap import Roadmap
from src.models.theme import Theme
from src.models.feature import Feature
from src.models.epic import Epic
from src.models.user_story import UserStory
from src.models.task import Task
from src.models.sprint import Sprint

def test_database():
    # Start a new database session
    db: Session = SessionLocal()

    # Insert a new project
    new_project = Project(name="Test Project", description="Project for testing relationships")
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    # Insert related models and verify relationships
    new_vision = Vision(project_id=new_project.id, name="Vision 1", details="Initial Vision")
    db.add(new_vision)

    # Insert a Roadmap with the project's ID
    new_roadmap = Roadmap(project_id=new_project.id, name="Roadmap 1", description="Initial Roadmap")
    db.add(new_roadmap)

    new_theme = Theme(project_id=new_project.id, name="Theme 1", description="Primary theme", order=1)
    db.add(new_theme)
    db.commit()  # Commit new_theme to get its ID
    db.refresh(new_theme)

    new_feature = Feature(theme_id=new_theme.id, name="Feature 1", description="First feature", status="active")
    db.add(new_feature)
    db.commit()  # Commit new_feature to get its ID
    db.refresh(new_feature)

    # Now we can safely add the Epic with new_feature's ID
    new_epic = Epic(feature_id=new_feature.id, name="Epic 1", description="An epic description", status="active")
    db.add(new_epic)
    db.commit()  # Commit new_epic to get its ID
    db.refresh(new_epic)

    # Now that new_epic is committed, we can add a UserStory with the epic's ID
    new_user_story = UserStory(
        epic_id=new_epic.id,
        description="A user story",
        acceptance_criteria="Criteria 1",
        status="open",
        estimate=3,
        value="high"
    )
    db.add(new_user_story)

    new_sprint = Sprint(project_id=new_project.id, name="Sprint 1", status="active")
    db.add(new_sprint)
    db.commit()
    db.refresh(new_sprint)

    new_task = Task(user_story_id=new_user_story.id, sprint_id=new_sprint.id, description="A task", status="open", estimate=2, type="development")
    db.add(new_task)
    db.commit()

    # Query to confirm relationships
    print("Project:", new_project)
    print("Project Visions:", new_project.visions)
    print("Project Themes:", new_project.themes)
    print("Theme Features:", new_theme.features)
    print("Feature Epics:", new_feature.epics)
    print("Epic User Stories:", new_epic.user_stories)
    print("User Story Tasks:", new_user_story.tasks)
    print("Sprint Tasks:", new_sprint.tasks)

    # Close the session
    db.close()

if __name__ == "__main__":
    test_database()


