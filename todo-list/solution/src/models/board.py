from src.models.task import Task
from src.models.person import Person
from typing import List
from datetime import datetime
from src.models.employee import Employee


class Board:
    ''' Representation of what a virtual board containing contributors and unassigned tasks
    '''
    def __init__(self):
        self.people: List[Person] = [] 
        self.backlog: List[Task] = []
        self.task_id_counter = 0

    def add_task(self, bio: str, author: Person, due_date: datetime) -> None:
        '''Add a task to the backlog.'''
        task = Task(id = self._get_next_task_id(),
        bio = bio,
        author = author,
        due_date=due_date)
        self.backlog.append(task)

    def get_backlog(self) -> List[Task]:
        '''get unasssigned tasks'''
        return self.backlog


    def mark_task_done(self, task_id: int) -> bool:
        '''Marked Task as done.'''
        for  p in self.people:
            if not isinstance(p, Employee):
                continue
            
            possible_task = p.get_task_by_id(task_id)
            if possible_task:
                return p.mark_task_as_complete(possible_task)
        
        return False # this task_id does not correspond to a ongoing task
            

    def _get_next_task_id(self) -> int:
        self.task_id_counter += 1
        return self.task_id_counter

    def add_contributor(self, contributor: Person) -> None:
        '''Add a Person as a contributor to the board.'''
        self.people.append(contributor)

    
    def get_contributors(self, only_employees: bool = True) -> List[Person]:
        '''Get contributors.
        Args:
        only_empployyes (bool): if true, only get contributors that are of type Employee,
        '''
        if not only_employees:
            return self.people
        
        contributors = []
        for p in self.people:
            if isinstance(p, Employee):
                contributors.append(p)
        return contributors
            
    