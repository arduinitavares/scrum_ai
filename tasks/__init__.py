"""
Initializes the tasks package by importing and exposing tasks for the Product Owner 
and Scrum Master agents.

These tasks are used by the CrewAI framework to define the actions each agent will perform
within the Scrum AI process.
"""

from .product_owner_tasks import (
    define_requirements_task,
    prioritize_backlog_task,
    gather_feedback_task,
    update_backlog_task
)

from .scrum_master_tasks import (
    facilitate_sprint_planning_task,
    conduct_daily_standup_task,
    remove_impediments_task
)

__all__ = [
    "define_requirements_task",
    "prioritize_backlog_task",
    "gather_feedback_task",
    "update_backlog_task",
    "facilitate_sprint_planning_task",
    "conduct_daily_standup_task",
    "remove_impediments_task"
]
