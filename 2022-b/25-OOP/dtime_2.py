class DTime:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        if not self._check_valid_time(hours=hours, minutes=minutes, seconds=seconds):
            raise ValueError(f'the time {hours:02d}:{minutes:02d}:{seconds:02d} is not valid')
        
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        

    def _check_valid_time(self, hours: int, minutes: int, seconds: int) -> bool:
        
        is_valid_hour = 0 <= hours < 24
        is_valid_minute = 0 <= minutes < 60
        is_valid_second = 0 <= seconds < 60

        return is_valid_hour and is_valid_minute and is_valid_second

    
    def get_hour(self) -> int:
        return self._hours

    def get_minutes(self) -> int:
        return self._minutes

    def get_seconds(self) -> int:
        return self._seconds


    def __str__(self) -> str:
        return  f'{self.get_hour():02d}:{self.get_minutes():02d}:{self.get_seconds():02d}'

    def __repr__(self) -> str:
        return f'DTime({self.get_hour()}, {self.get_minutes()}, {self.get_seconds()})'

    
    def __eq__(self, other) -> bool:
        if not isinstance(other, DTime):
            return False

        return (
            self.get_hour() == other.get_hour() and 
            self.get_minutes == other.get_minutes() and 
            self.get_seconds() == other.get_seconds()
        )

    def __gt__(self, other) -> bool:
        
        self_time = self.get_hour() * 3600 + self.get_minutes() * 60 + self.get_seconds()

        other_time = other.get_hour() * 3600 + other.get_minutes() * 60 + other.get_seconds()

        return self_time > other_time


    def __lt__(self, other) -> bool:
        
        if self == other:
            return False

        return not (self > other)


    def __ge__(self, other) -> bool:
        
        if self == other:
            return True

        return self > other 

    
    def __le__(self, other) -> bool:
        
        return not( self > other)



