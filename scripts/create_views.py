from sqlalchemy import create_engine, text
from src.db.session import engine

def create_views():
    # Define the views
    views = {
        "project_overview": """
            CREATE OR REPLACE VIEW project_overview AS
            SELECT 
                p.id AS project_id,
                p.name AS project_name,
                p.description AS project_description,
                COUNT(DISTINCT t.id) AS total_themes,
                COUNT(DISTINCT f.id) AS total_features,
                COUNT(DISTINCT e.id) AS total_epics,
                COUNT(DISTINCT us.id) AS total_user_stories
            FROM 
                projects p
            LEFT JOIN themes t ON t.project_id = p.id
            LEFT JOIN features f ON f.theme_id = t.id
            LEFT JOIN epics e ON e.feature_id = f.id
            LEFT JOIN user_stories us ON us.epic_id = e.id
            GROUP BY 
                p.id, p.name, p.description;
        """,
        
        "sprint_progress_summary": """
            CREATE OR REPLACE VIEW sprint_progress_summary AS
            SELECT 
                s.id AS sprint_id,
                s.name AS sprint_name,
                p.name AS project_name,
                COUNT(t.id) AS total_tasks,
                SUM(CASE WHEN t.status = 'done' THEN 1 ELSE 0 END) AS tasks_completed,
                SUM(CASE WHEN t.status = 'open' THEN 1 ELSE 0 END) AS tasks_open,
                SUM(CASE WHEN t.status = 'in_progress' THEN 1 ELSE 0 END) AS tasks_in_progress
            FROM 
                sprints s
            JOIN projects p ON s.project_id = p.id
            LEFT JOIN tasks t ON t.sprint_id = s.id
            GROUP BY 
                s.id, s.name, p.name;
        """,
        
        "user_story_task_summary": """
            CREATE OR REPLACE VIEW user_story_task_summary AS
            SELECT 
                us.id AS user_story_id,
                us.description AS user_story_description,
                e.name AS epic_name,
                f.name AS feature_name,
                t.description AS task_description,
                t.status AS task_status,
                t.estimate AS task_estimate
            FROM 
                user_stories us
            JOIN epics e ON us.epic_id = e.id
            JOIN features f ON e.feature_id = f.id
            LEFT JOIN tasks t ON t.user_story_id = us.id
            ORDER BY 
                us.id, t.id;
        """,
        
        "high_priority_tasks": """
            CREATE OR REPLACE VIEW high_priority_tasks AS
            SELECT 
                t.id AS task_id,
                t.description AS task_description,
                us.description AS user_story,
                s.name AS sprint,
                p.name AS project,
                t.status,
                t.estimate
            FROM 
                tasks t
            JOIN user_stories us ON t.user_story_id = us.id
            JOIN sprints s ON t.sprint_id = s.id
            JOIN projects p ON s.project_id = p.id
            WHERE 
                t.status IN ('open', 'in_progress')
                AND t.type = 'high'
            ORDER BY 
                p.name, s.name, t.estimate DESC;
        """,
        
        "project_timeline_status": """
            CREATE OR REPLACE VIEW project_timeline_status AS
            SELECT 
                p.id AS project_id,
                p.name AS project_name,
                p.start_date,
                p.end_date,
                p.status,
                CASE 
                    WHEN p.end_date < CURRENT_DATE THEN 'Past Due'
                    WHEN p.start_date > CURRENT_DATE THEN 'Upcoming'
                    ELSE 'In Progress'
                END AS project_timeframe_status
            FROM 
                projects p
            ORDER BY 
                p.end_date DESC;
        """
    }
    
    # Connect to the database and create each view
    with engine.connect() as connection:
        for view_name, view_sql in views.items():
            print(f"Creating view {view_name}...")
            connection.execute(text(view_sql))
        print("Views created successfully!")

if __name__ == "__main__":
    create_views()
