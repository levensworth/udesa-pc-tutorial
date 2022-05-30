from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from src.models.task import Task
    from solution.src.models.employee import Employee

from src.models.person import Person

class Director(Person):
    
    def assing_task(self, task: Task, assignee: Employee) -> Task:
        '''Given a task and an employee, assign task to the person.'''

        assignee.add_task(task)
        return task