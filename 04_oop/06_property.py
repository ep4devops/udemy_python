class Student:
    def __init__(self, name, school):
        # Called properties
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

#Extends Student
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
    @property
    # Turns a method into a property
    def weekly_salary(self):
        return self.salary * 37.5

wstudent1 = WorkingStudent('Enrico', 'TGG', 15)
print(wstudent1.weekly_salary)
# Ohne
# <bound method WorkingStudent.weekly_salary of <__main__.WorkingStudent object at 0x0000017999D4D6A0>>
# Mit property
# 562.5