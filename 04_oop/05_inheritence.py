class Student:
    def __init__(self, name, school):
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
    
    def weekly_salary(self):
        return self.salary * 37.5

wstudent1 = WorkingStudent('Enrico', 'TGG', 15.5)
wstudent1.marks.append(80)
print(wstudent1.average())
print(wstudent1.weekly_salary())