

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_basic_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")



class student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_details(self):
        print("\n--- Student Details ---")
        self.display_basic_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")



class Professor(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_d(self):
        print("\n--- Professor Details ---")
        self.display_basic_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

name = "vamsi"
age = 22
student_id = "AA214563"
course = "computer science"
employee_id = "ASD123"
department = "ccbb"

num = student(name,age,student_id,course)
num.display_basic_info()
num.display_details()
date =Professor(name,age,employee_id,department)
date.display_d()














