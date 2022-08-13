from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from src.models.task import Task

from src.models.person import Person
from typing import List, Optional

from datetime import datetime

class Employee(Person):
    def __init__(self, name: str, surname: str, email: str):
        super().__init__(name=name, surname=surname, email=email)
        self.tasks: List[Task] = []
        self.completed_tasks: List[Task] = []


    def get_task_by_id(self, task_id) -> Optional[Task]:
        '''Given an id, get task (only if it belongs to the employee)'''
        for t in self.tasks:
            if t.get_id() == task_id:
                return t 
        
    def get_tasks_by_due_date(self, from_date: Optional[datetime] = None) -> List[Task]:
        '''Get a sorted list of pending tasks for the employee.'''
        # only check tasks that aren't expired
        filtered_tasks = self._filter_tasks(self._is_task_older_than, from_date)
        filtered_tasks.sort()
        return filtered_tasks
    
    def mark_task_as_complete(self, task: Task) -> bool:
        '''Given a task, mark it as done.'''
        try:
            self.tasks.remove(task)
            task.completed = True
            self.completed_tasks.append(task)
            return task.mark_as_completed()
        except ValueError:
            # the task does not exists
            return False

    def add_task(self, task: Task) -> bool:
        '''Add a new task.'''
        self.tasks.append(task)
        task.assign_to(self)
        return True

    def _filter_tasks(self, predicate, *args) -> List[Task]:
        # sourcery skip: for-append-to-extend, inline-immediately-returned-variable, list-comprehension
        tasks = []

        for task in self.tasks:
            if predicate(task, *args):
                tasks.append(task)

        return tasks 

    def _is_task_older_than(self, task: Task, from_date: datetime) -> bool:
        return task._get_time_until_due(from_date).seconds > 0
