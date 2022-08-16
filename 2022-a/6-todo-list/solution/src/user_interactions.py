from typing import List, Dict
from src.models.board import Board
from src.models.person import Person
from src.models.employee import Employee
from src.models.task import Task
import datetime

def create_employee() -> Employee:
    name = input('employee name:> ')
    surname = input('employee surname:> ')
    email = input('employee email:> ')
    return Employee(name, surname, email)


def create_new_task(person: Person, board: Board):
    bio = input('what is the task about? ')
    due_date = input('when is it due for? [provide a date in the format dd-mm-yyyy hh:mm]')
    due_datetime = datetime.datetime.strptime(due_date, '%d-%m-%Y %H:%M')
        
    person.create_task(board, bio, due_datetime)


def show_tasks(tasks: List[Task]) -> None:
    if len(tasks) == 0:
        print('there are no tasks')
    for task in tasks:
        print('==>', task)


def get_task_id(max_id: int) -> int:
    while True:
        task_id = int(input('which task should be marked as finished> [type task id] '))
        if task_id >= 0 and task_id <= max_id:
            return task_id
        print('unrecognized  task')


def select_person(people: List[Person], type_name: str) -> Person:
    print(f'Please select a {type_name} from the following list:')
    candidates = { str(p): p for p in people}
    return show_commands(candidates)


def show_commands(commands: Dict):
    commands_idx = []
    for idx, command in enumerate(commands):
        commands_idx.append((idx, command))
    
    for idx, command in commands_idx:
        print(f'[{idx}] {command}')

    
    while True:
        option = input('plase, select an option :> ')
        if int(option) >= 0 and int(option) < len(commands):
            _, command_name = commands_idx[int(option)]
            return commands[command_name]

        print(f'option {option} not found')
