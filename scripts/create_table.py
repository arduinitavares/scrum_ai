import time
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy import text
from src.db.session import engine, Base
import src.models

def drop_dependent_views(connection):
    dependent_views = [
        "user_story_task_summary",
        "project_overview",
        "sprint_progress_summary",
        "high_priority_tasks",
        "project_timeline_status"
    ]
    
    for view in dependent_views:
        print(f"Dropping view {view} if it exists...")
        try:
            connection.execute(text(f"DROP VIEW IF EXISTS {view} CASCADE"))
        except SQLAlchemyError as e:
            print(f"Error dropping view {view}: {e}")

def recreate_tables():
    attempts = 3
    delay = 5  # seconds

    for attempt in range(attempts):
        try:
            with engine.begin() as connection:
                # Drop dependent views first
                drop_dependent_views(connection)
                
                # Drop all existing tables
                print("Dropping existing tables...")
                Base.metadata.drop_all(bind=engine)
                print("Creating database tables...")
                Base.metadata.create_all(bind=engine)
                print("Tables created successfully!")
                break  # Exit loop if successful
        except OperationalError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
        except SQLAlchemyError as e:
            print(f"Unexpected error: {e}")
            break  # Stop retrying if a non-recoverable error occurs

if __name__ == "__main__":
    recreate_tables()
