import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

def get_database():
    """
    Connects to the MongoDB instance and returns the database object.
    """
    client = MongoClient(MONGODB_URI)
    db = client['scrum_ai']  # Use your database name
    return db

def list_projects():
    """
    Lists all existing projects in the 'projects' collection.
    
    Returns:
        list: A list of project names.
    """
    db = get_database()
    project_collection = db['projects']
    projects = project_collection.find({}, {"name": 1})
    return [project['name'] for project in projects]

def is_project_exist(project_name):
    """
    Checks if a project entry exists in the 'projects' collection.
    
    Args:
        project_name (str): The name of the project.
        
    Returns:
        bool: True if the project exists, False otherwise.
    """
    db = get_database()
    project_collection = db['projects']
    return project_collection.count_documents({"name": project_name}) > 0

def create_project_entry(project_name, project_data):
    """
    Inserts a new project entry into the 'projects' collection.
    
    Args:
        project_name (str): The name of the project.
        project_data (dict): The project data to be inserted.
    """
    db = get_database()
    project_collection = db['projects']
    project_data['name'] = project_name
    project_collection.insert_one(project_data)

def get_project(project_name):
    """
    Retrieves a project entry from the 'projects' collection based on the project name.
    
    Args:
        project_name (str): The name of the project.
        
    Returns:
        dict: The project data if found, None otherwise.
    """
    db = get_database()
    project_collection = db['projects']
    return project_collection.find_one({"name": project_name})

def update_project_task(project_name, task_id, updated_task_data):
    """
    Updates a specific task in the project based on the task ID.
    
    Args:
        project_name (str): The name of the project.
        task_id (int): The ID of the task to update.
        updated_task_data (dict): The updated task data.
    """
    db = get_database()
    project_collection = db['projects']
    project_collection.update_one(
        {"name": project_name, "tasks.ID": task_id},
        {"$set": {"tasks.$": updated_task_data}}
    )
