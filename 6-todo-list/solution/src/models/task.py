from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from src.models.person import Person
    from src.models.employee import Employee

from datetime import datetime, timedelta

SUMMARY_LENGTH = 50

class Task:
    def __init__(self, id: int, bio: str, author: Person, due_date: datetime):
        self.id = id
        self.bio = bio
        self.author = author
        self.assignee = None
        self.due_date = due_date
        self.completed = False


    def get_id(self) -> int:
        return self.id

    def assign_to(self, assignee: Employee):
        self.assignee = assignee
        
    def mark_as_completed(self) -> bool:
        self.completed = True
        return self.completed

    def _get_time_until_due(self, from_date: datetime) -> timedelta:
        return (self.due_date - from_date)


    def get_summary(self) -> str:
        trailing_dots = '...' if len(self.bio) > SUMMARY_LENGTH else ''
        return f'{self.bio[:SUMMARY_LENGTH]} {trailing_dots}'

    def __repr__(self) -> str:
        time_left =  self._get_time_until_due(datetime.now())
        days_left = time_left.days
        hours_left = (time_left.seconds // (3600))% 24
        minutes_left = (time_left.seconds % 3600) // 60
        time_left_repr = f'{days_left} days | {hours_left} hours | {minutes_left} minutes'
        
        return f'Task: {self.id}\nBio: {self.bio}\nAssigned to: {self.assignee}\nCreated By: {self.author}\nDue at: {self.due_date} [time left: {time_left_repr}]'
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Task):
            raise ValueError('Trying to compare differente things')
        
        return self.due_date < other.due_date
            