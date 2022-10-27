from typing import Dict, List, Optional, Tuple

class Student:
    
    def __init__(self, name: str, id: int, email: str ='') -> None:
        self.__name = name
        self.__id = id 

        self.__email = email
        self.__subject_marks = {}
        self.__num_absenses = 0


    def set_email(self, email: str) -> None:
        self.__email = email

    def set_mark(self, typ: str, mark: int) -> None:
        # esto se ejecuta si todavía no hay notas de dicho tipo
        self.__subject_marks.setdefault(typ, [])

        self.__subject_marks[typ].append(mark)

    def set_absences(self, num: int) -> None:
        self.__num_absenses = num

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def get_email(self) -> str:
        return self.__email

    def get_absences(self) -> int:
        return self.__num_absenses

    def get_marks(self, typ: str) -> List[int]:
        return self.__subject_marks.get(typ, [])


class Course:

    def __init__(self, 
        name: str, 
        course_id: str, 
        u_degree: str, 
        professor: str
    ) -> None:

        self.__name = name
        self.__course_id = course_id
        self.__u_degree  = u_degree
        self.__professor = professor
        
        self.__students: Dict[int, Student] = {}

    
    def add_student(self, id: int, name: str, email: str ='') -> None:
        self.__students[id] = Student(name=name, id=id)

    def add_mark(self, id: int, typ: str, mark: int) -> None:
        student = self.__get_student(id)
        if not student:
            raise ValueError('No student with id' + str(id))
        
        student.set_mark(typ=typ, mark=mark)

    def set_email(self, id: int, email: str) -> None:
        student = self.__get_student(id)
        if not student:
            raise ValueError('No student with id' + str(id))
        
        student.set_email(email=email)

    def set_new_absences(self, id: int, num: int) -> None:
        student = self.__get_student(id)
        if not student:
            raise ValueError('No student with id' + str(id))
        
        student.set_absences(num)


    def sort_students(self, method: str) -> List[Tuple[int, Student]]:
        students = list(self.__students.items())
        key_sort = None
        reverse = False
        if method == 'nombre':
            key_sort = lambda stu_t: stu_t[1].get_name()
        
        elif method == 'legajo':
            key_sort = lambda stu_t: stu_t[1].get_id()
        
        elif method == 'ausentes':
            key_sort = lambda stu_t: stu_t[1].get_absences()
            reverse = True
        
        else:
            raise ValueError('Invalid Option ' + method)

        students.sort(key = key_sort, reverse=reverse)
        
        return students

    def __get_student(self, id: int) -> Optional[Student]:
        return self.__students.get(id, None)



    
        


            


