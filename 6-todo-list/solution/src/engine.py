from typing import List
from src.models.director import Director
from src.models.task import Task
from src.models.person import Person
from src.models.board import Board
from src.models.employee import Employee
from src.user_interactions import (
    create_employee, 
    create_new_task, 
    show_commands, 
    show_tasks, 
    get_task_id, 
    select_person
)
from datetime import datetime
import pickle

FILE_NAME = 'board_savepoint.acme'


class Engine:
    def __init__(self):
        self.board = self._get_board()
        self.running = False


    def _get_board(self) -> Board:
        try:
            return self._load_model()
        except Exception:
            # there is no model to get
            board = Board()
            board.add_contributor(Director('santiago', 'Bassani', 'dirforu@acme.com'))
            return board

    def run(self):
        print('welcome, this is a virtual Board for the Marketing team at Acme SA.')
        
        commands = {
            'save': self._save_model_command,
            'new_employee': self._create_employee_command,
            'new_task': self._create_new_task_command, 
            'show_employee_tasks': self._show_employee_tasks_command,
            'assing_task': self._assing_task_commnd,
            'mark_task_as_done': self._mark_task_as_done_command,
            'quit': self._finish_run_command
        }    
        self.running = True

        while self.running:
            command_fn = show_commands(commands)
            command_fn()
        
            
    def _finish_run_command(self):
        self.running = False

    def _save_model_command(self):
        fd = open(FILE_NAME, 'wb')
        pickle.dump(self.board, fd)

    def _load_model(self) -> Board:
        fd = open(FILE_NAME, 'rb')
        return pickle.load(fd)

    def _create_employee_command(self):
        employee = create_employee()
        self.board.add_contributor(employee)
    
    def _create_new_task_command(self):
        create_new_task(self._get_contributor(only_employees=False, type_name='Author'), self.board)
        
    def _show_employee_tasks_command(self):
        
        contributor: Employee = self._get_contributor() # type: ignore
        tasks = contributor.get_tasks_by_due_date(datetime.now())
        show_tasks(tasks)

    def _assing_task_commnd(self):
        director = None
        while director is None:
            director = self._get_contributor(only_employees=False, type_name='Director')
            if not isinstance(director, Director):
                print('Only Directors can assign tasks')
                director = None
        
        tasks = {f'{task.get_id()}: {task.bio}': task for task in self.board.get_backlog()}
        selected_task: Task  = show_commands(tasks)
        
        assignee: Employee = self._get_contributor() # type: ignore
        
        director.assing_task(selected_task, assignee) # type: ignore
        
    def _mark_task_as_done_command(self):
        task_id = get_task_id(self.board.task_id_counter)
        self.board.mark_task_done(task_id)

    def _get_contributor(self, only_employees: bool = True, type_name: str = 'Employee') -> Person:
        contributors = self.board.get_contributors(only_employees=only_employees)
        
        return select_person(contributors, type_name)
        
    