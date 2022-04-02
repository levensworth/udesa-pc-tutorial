
from curses import ERR
from typing import Tuple

PARSING_DAY = 0
PARSING_MONTH = 1
ERROR = -1

SEPARATOR_SEMICOL = ':'
SEPARATOR_DASH = '-'
SEPARATOR_SLASH = '/'

def parse_date(possible_date: str) -> Tuple[int, int]:
    '''
    Given a possible date, try to parse the string looking for 
    the pattenr: dd[separator]mm
    Params:
    - passible_date: str -> this is the string to parse

    returns a tuple of 2 integers, representing the day and month or None in case of error.
    '''
    
    parse_state = PARSING_DAY
    
    day = ''
    month = ''
    for char in possible_date:
        if parse_state == PARSING_DAY:
            if char.isnumeric():
                day += char
            elif char in (SEPARATOR_DASH, SEPARATOR_SEMICOL, SEPARATOR_SLASH):
                parse_state = PARSING_MONTH
            else:
                parse_state = ERROR
                continue

            continue

        if parse_state == PARSING_MONTH:
            if char.isnumeric():
                month += char
            else:
                parse_state = ERROR
                continue
            continue

        if parse_state == ERROR:
            return None
                
    if parse_state == ERROR or len(day) == 0 or len(month) == 0:
        return None

    # If the loop concluded, it means that we succeded
    return (int(day), int(month))

