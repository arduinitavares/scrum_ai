"""
main.py

Entry point for running the scrum_ai project, which sets up and executes an AI-driven
Scrum crew to autonomously manage Scrum roles and processes for software development.
"""

from crews.scrum_crew import create_scrum_crew

def main():
    """
    Initializes and runs the AI-driven Scrum crew based on the project scope.

    The project scope is to create a Scrum AI crew that supports software development
    by managing product backlogs, sprint planning, and task prioritization autonomously.

    Returns:
        None
    """
    # Define the project scope for the Scrum AI crew
    project_scope = (
        "Create an AI-driven Scrum crew to autonomously manage software development tasks, "
        "including backlog management, sprint planning, and task prioritization."
    )

    # Create and execute the Scrum crew
    scrum_crew = create_scrum_crew(project_scope)
    scrum_crew.run()

if __name__ == "__main__":
    main()
