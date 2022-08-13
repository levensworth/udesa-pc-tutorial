from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.board import Board

from datetime import datetime


class Person:
    def __init__(self, name: str, surname: str, email: str):
        self.name = name
        self.surname = surname
        self.email = email

    def get_name(self) -> str:
        return self.name
    
    def get_surname(self) -> str:
        return self.surname

    def get_email(self) -> str:
        return self.email
    
    def create_task(self, board: Board, bio: str, due_date: datetime) -> None:
        board.add_task(bio, self, due_date)
        
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.get_name()} {self.get_surname()} =>  {self.get_email()}'