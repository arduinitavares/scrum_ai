"""
Defines the ProductOwnerAgent class responsible for managing the product backlog
and prioritizing features based on the Scrum AI process using the CrewAI framework.
"""

from crewai import Agent

class ProductOwnerAgent(Agent):
    """
    Represents the Product Owner agent in the Scrum process, responsible for defining
    product requirements, prioritizing the product backlog, and incorporating stakeholder feedback.
    """
    name = "Product Owner"
    role = "Product Owner"
    goal = "Manage the product backlog and prioritize tasks"
    backstory = '''Responsible for ensuring that the development
    team works on tasks that deliver the most value'''

    def __init__(self, name=name, role=role, goal=goal, backstory=backstory, **kwargs):
        """
        Initializes the Product Owner agent with the specified attributes.

        Args:
            name (str): Name of the agent. Default is "Product Owner".
            role (str): Role of the agent in the Scrum process.
            goal (str): Goal that the Product Owner agent aims to achieve.
            backstory (str): A brief background about the agent.
            **kwargs: Additional keyword arguments passed to the Agent base class.
        """
        super().__init__(name=name, role=role, goal=goal, backstory=backstory, **kwargs)
        self.product_backlog = []

    def define_product_requirements(self, project_scope):
        """
        Defines product requirements based on the provided project scope.

        Args:
            project_scope (str): A description of the project's objectives and scope.
        """
        self.product_backlog = self.generate_product_backlog(project_scope)
        print("Product requirements defined.")

    def generate_product_backlog(self, project_scope):
        """
        Generates a product backlog based on the project scope. This method can be extended
        to parse and utilize the project_scope for generating dynamic backlog items.

        Args:
            project_scope (str): A description of the project's objectives and scope.

        Returns:
            list: A list of product backlog items.
        """
        # For simplicity, backlog items are predefined,
        # but project_scope can be used for dynamic generation
        return [
            {"id": 1, "title": f"{project_scope} - Feature A", "priority": 1},
            {"id": 2, "title": f"{project_scope} - Feature B", "priority": 2},
            {"id": 3, "title": f"{project_scope} - Feature C", "priority": 3}
        ]

    def prioritize_backlog(self):
        """
        Prioritizes the product backlog based on the 'priority' key.
        """
        self.product_backlog.sort(key=lambda item: item['priority'])
        print("Product backlog prioritized.")

    def gather_stakeholder_feedback(self):
        """
        Gathers feedback from stakeholders.

        Returns:
            str: The gathered stakeholder feedback.
        """
        feedback = "Positive feedback from stakeholders."
        print(f"Stakeholder feedback: {feedback}")
        return feedback

    def update_backlog_with_feedback(self, feedback):
        """
        Updates the product backlog based on the provided stakeholder feedback.

        Args:
            feedback (str): The feedback received from stakeholders.
        """
        # Placeholder logic to update the backlog with feedback
        print("Product backlog updated with feedback:", feedback)
