# crews/scrum_crew.py

from crewai  import Crew
from agents import ProductOwnerAgent, ScrumMasterAgent
from tasks import (
    define_requirements_task,
    prioritize_backlog_task,
    gather_feedback_task,
    update_backlog_task,
    facilitate_sprint_planning_task,
    conduct_daily_standup_task,
    remove_impediments_task
)

def create_scrum_crew(project_scope):
    # Instantiate agents
    product_owner = ProductOwnerAgent()
    scrum_master = ScrumMasterAgent()

    # Create the crew
    scrum_crew = Crew(agents=[product_owner, scrum_master])

    # Assign tasks to the Product Owner
    scrum_crew.assign_task(product_owner, define_requirements_task, project_scope=project_scope)
    scrum_crew.assign_task(product_owner, prioritize_backlog_task)
    scrum_crew.assign_task(product_owner, gather_feedback_task)
    scrum_crew.assign_task(product_owner, update_backlog_task)

    # Assign tasks to the Scrum Master
    scrum_crew.assign_task(scrum_master, facilitate_sprint_planning_task, product_backlog=product_owner.product_backlog)
    scrum_crew.assign_task(scrum_master, conduct_daily_standup_task, team_members=[])  # Provide team_members list
    scrum_crew.assign_task(scrum_master, remove_impediments_task, impediments_list=[])

    return scrum_crew
