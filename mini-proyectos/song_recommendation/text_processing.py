from typing import Dict, List, Union
import csv 
import os
from unittest import result 

def load_csv(
    file_path: str, 
    delimiter: str = ',', 
    has_header: bool = True,
    try_casting: bool = True

) -> List[Dict]:
    '''
    This function laods a csv file from the given path. It accepts both csv with headers and without them.
    
    Args:
        file_path: (str) the path to the given csv file.
        delimiter: (str) the string delimiter between columns of the csv.
        has_headers: (bool) flag to indicate if the file has headers. [Default True]
    
    Output:
    Returns a List of dictionaries representing each row. The keys of each dictionary ar the 
    column name.
    
    Throws:
    - FileNotFoundError
    

    '''    
    if not os.path.exists(file_path):
        print(f'The path {file_path} does not exists!')
        raise FileNotFoundError
    
    results = []

    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        
        if has_header:
            headers = next(csv_reader)
            
            
        for row in csv_reader:
            if try_casting:
                mapped_row = list(map(lambda item: cast_to_num(item), row))
            else:
                mapped_row = row
                
            new_row = { key : item for key, item in zip(headers, mapped_row)}
            results.append(new_row)

    return results
        


def cast_to_num(value: str) -> Union[str, int, float]:

    int_val = None
    float_val = None

    try:
        int_val = int(value)    
    except ValueError:
        try:
            float_val = float(value)
        except ValueError:
            pass    

    if int_val is not None:
        return int_val

    if float_val is not None:
        return float_val
    
        
    return value


    
    
    


