class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Lecturer(Person):
    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)

class Student(Person):
    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group:str):
        self.group = group

class Group:
    def __init__(self,name:str, limit:int):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
    def get_name(self):
        return self.name
    def get_limit(self):
        return self.limit
    def get_students(self):
        return self.students
    def get_limit_lecturers(self):
        max_lecturers = max(1,len(self.students)//10)
        return max_lecturers
    def add_student(self, student):
        if len(self.students)<self.limit:
            self.students.append(student)
            student.set_group(self)
            return True 
        return False
    def add_lecturer(self, lecturer):
        if len(self.lecturers)<self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True 
        return False


class Course:
    def __init__(self, name:str):
        self.name = name
        self.groups = []

    def register(self, student): 
        for group in self.groups:
            if group.add_student(student):
                return 
            
    def get_groups(self):
        return self.groups
    
    def add_group(self, group):
        self.groups.append(group)