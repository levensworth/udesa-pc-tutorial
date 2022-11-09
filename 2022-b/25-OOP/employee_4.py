from dtime_3 import DTime


class Employee:
    def __init__(self, id: str, name: str, sign_in_time: DTime, sign_out_time: DTime) -> None:
        self.id = id
        self.name = name
        self.sign_in_time = sign_in_time
        self.sign_out_time = sign_out_time

    def __str__(self) -> str:
        return f'Emplyee[{self.id}] {self.name}  sign_id @ {self.sign_in_time}  | sign_out @ {self.sign_out_time}'
    
