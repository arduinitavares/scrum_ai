"""
Defines tasks for the Scrum Master agent using the CrewAI framework.

Each task represents a key responsibility of the Scrum Master, such as facilitating sprint planning,
conducting daily stand-ups, and removing impediments to ensure the team can work effectively.
"""

from crewai import Task

# Define tasks for the Scrum Master
facilitate_sprint_planning_task = Task(
    name="Facilitate Sprint Planning",
    description="Assist the team in planning the upcoming sprint.",
    execute=lambda agent, **kwargs: agent.facilitate_sprint_planning(
        kwargs.get('product_backlog')
    ),
    expected_output="A defined and prioritized sprint backlog for the upcoming sprint."
)

conduct_daily_standup_task = Task(
    name="Conduct Daily Stand-up",
    description="Check in with the team to monitor progress and identify impediments.",
    execute=lambda agent, **kwargs: agent.conduct_daily_standup(
        kwargs.get('team_members')
    ),
    expected_output="Daily status updates from team members and identified impediments."
)

remove_impediments_task = Task(
    name="Remove Impediments",
    description="Identify and resolve any impediments blocking the team.",
    execute=lambda agent, **kwargs: agent.identify_and_remove_impediments(
        kwargs.get('impediments_list')
    ),
    expected_output="A list of resolved impediments that were blocking team progress."
)
