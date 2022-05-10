from datetime import datetime



def time_it(f, *args) -> int:
    init  = datetime.now()
    f(*args)
    finish = datetime.now()
    return (finish - init).microseconds
    