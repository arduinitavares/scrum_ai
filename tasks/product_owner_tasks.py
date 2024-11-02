"""
Defines tasks for the Product Owner agent using the CrewAI framework.

Each task represents a key responsibility of the Product Owner, such as defining requirements,
prioritizing the backlog, gathering stakeholder feedback, and updating the backlog.
"""
from crewai import Task

# Define tasks for the Product Owner
define_requirements_task = Task(
    name="Define Requirements",
    description="Define product requirements based on the project scope.",
    execute=lambda agent, **kwargs: agent.define_product_requirements(kwargs.get('project_scope')),
    expected_output="A list of defined product requirements."
)

prioritize_backlog_task = Task(
    name="Prioritize Backlog",
    description="Prioritize the product backlog.",
    execute=lambda agent, **kwargs: agent.prioritize_backlog(),
    expected_output="A prioritized product backlog."
)

gather_feedback_task = Task(
    name="Gather Stakeholder Feedback",
    description="Gather feedback from stakeholders.",
    execute=lambda agent, **kwargs: agent.gather_stakeholder_feedback(),
    expected_output="Stakeholder feedback collected."
)

update_backlog_task = Task(
    name="Update Backlog with Feedback",
    description="Update the product backlog based on stakeholder feedback.",
    execute=lambda agent, **kwargs: agent.update_backlog_with_feedback(kwargs.get('feedback')),
    expected_output="An updated product backlog with feedback incorporated."
)
