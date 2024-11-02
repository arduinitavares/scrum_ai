from sqlalchemy import text
from src.db.session import engine

def show_view_data():
    views = ["project_overview", "sprint_progress_summary", 
             "user_story_task_summary", "high_priority_tasks", "project_timeline_status"]

    with engine.connect() as connection:
        for view in views:
            print(f"\nData from view: {view}")
            result = connection.execute(text(f"SELECT * FROM {view}")).fetchall()

            # Display column names
            if result:
                columns = result[0].keys()
                print("\t".join(columns))

                # Display each row of data
                for row in result:
                    print("\t".join(str(value) for value in row))
            else:
                print("No data available in this view.")

if __name__ == "__main__":
    show_view_data()
