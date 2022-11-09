from employee_4 import Employee
from dtime_3 import DTime
from typing import Optional


class TimeManager:
    def __init__(
        self, 
        day_start_time: DTime,
        day_end_time: DTime
    ) -> None:
        self._employees = []
        self._start_time = day_start_time
        self._end_time = day_end_time


    def add_employee(self, employee: Employee) -> None:
        self._employees.append(employee)

    def print_employee_registry(self) -> None:
        
        for employee in self._employees:
            delta_start = self._compute_workday_start(employee)
            delta_end = self._compute_workday_end(employee)
            print('='*80)
            print(f'{employee}')
            if delta_start is not None:
                print(f'Started: {delta_start} shifted from the begining of the day')
            else:
                print('Started on time')
            
            if delta_end is not None:
                print(f'Ended: {delta_end} shifted from the end of the day')
            else:
                print('Ended on time')

            

    
    def _compute_workday_start(self, employee: Employee) -> Optional[DTime]:
        if employee.sign_in_time <= self._start_time:
            return None
        return employee.sign_in_time - self._start_time


    def _compute_workday_end(self, employee: Employee) -> Optional[DTime]:
        if employee.sign_out_time >= self._end_time:
            return None
        
        return self._end_time - employee.sign_out_time


    

def main():

    start = DTime(9,0, 0)
    end = DTime(19, 0, 0)

    manager = TimeManager(start, end)

    manager.add_employee(Employee('1', 'sofia', DTime(9, 0, 0), DTime(19, 0, 0)))
    manager.add_employee(Employee('2', 'juan', DTime(9, 0, 0), DTime(17, 0, 0)))
    manager.add_employee(Employee('3', 'santi', DTime(11, 0, 0), DTime(13, 0, 0)))

    manager.print_employee_registry()

if __name__ == '__main__':
    main()
