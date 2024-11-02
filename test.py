import os
from crewai import Agent, Task, Crew, Process
from tools.database_tools import list_projects, create_project_entry, get_project, is_project_exist
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up environment variables for API keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define the Product Owner agent with a dynamic responsibility
product_owner = Agent(
    role='Product Owner',
    goal='Manage and prioritize the product backlog to maximize the value delivered to stakeholders.',
    backstory="""You are a dedicated Product Owner with deep knowledge of the product vision.
    You prioritize tasks based on stakeholder needs and ensure that the development team works
    on the most valuable features.""",
    verbose=True,
    allow_delegation=False
)

def interactive_project_management(agent):
    """
    Engages with the user interactively to either select an existing project or create a new one.
    """
    projects = list_projects()
    
    if projects:
        print("Hello! I see there are some projects in progress:")
        for idx, project in enumerate(projects, 1):
            print(f"{idx}. {project}")

        choice = input("Do you want to discuss an existing project or start a new one? (existing/new): ").strip().lower()

        if choice == "existing":
            project_choice = int(input(f"Please select a project (1-{len(projects)}): "))
            selected_project = projects[project_choice - 1]
            print(f"Great! Let's continue working on the '{selected_project}' project.")
            return selected_project

    # Proceed with creating a new project
    print("\nLet's start a new project.")
    project_name = input("What is the name of the new project? ").strip()

    if is_project_exist(project_name):
        print(f"The project '{project_name}' already exists.")
        return project_name
    
    print("We'll now gather information for the project using Scrum practices.")

    tasks = []
    add_more_tasks = 'yes'
    task_id = 1

    while add_more_tasks.lower() == 'yes':
        print("\nPlease provide the following details for a new task:")

        theme = input("Theme: ")
        feature = input("Feature: ")
        epic = input("Epic: ")
        user_story = input("User Story: ")
        task_description = input("Task Description: ")
        task_type = input("Task Type (Requirement, Design, etc.): ")
        status = input("Status (To Do, In Progress, Done): ")
        estimate = int(input("Estimate (in hours or story points): "))
        value = input("Value (High, Medium, Low): ")
        sprint = input("Sprint: ")

        task = {
            "Order": task_id,
            "ID": task_id + 1000,  # Example ID increment
            "Themes": theme,
            "Feature": feature,
            "Epic": epic,
            "User Story": user_story,
            "Task": task_description,
            "Type": task_type,
            "Status": status,
            "Estimate": estimate,
            "Value": value,
            "Sprint": sprint
        }
        
        tasks.append(task)
        task_id += 1
        add_more_tasks = input("Do you want to add another task? (yes/no): ")

    project_data = {
        "tasks": tasks
    }

    create_project_entry(project_name, project_data)
    print(f"Project '{project_name}' created successfully with the provided tasks!")
    return project_name

# Define a task for the Product Owner to manage the interactive process
interactive_management_task = Task(
    description="Interact with the user to manage the project selection or creation process.",
    expected_output="A project selected or created for further Scrum activities.",
    execute=lambda agent, **kwargs: interactive_project_management(agent),
    agent=product_owner
)

# Create the crew with the interactive management task
scrum_crew = Crew(
    agents=[product_owner],
    tasks=[interactive_management_task],
    verbose=True,
    process=Process.sequential  # Execute tasks sequentially
)

# Start the Scrum AI process
scrum_crew.kickoff()

print("######################")
