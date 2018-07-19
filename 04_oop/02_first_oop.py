class Student:
    # Dunder Functions (Double undersore)
    def __init__(self, new_name, new_grades):
        # Self blank Onject, self.name creates a var in blank object
        
        #Called Property
        self.name = new_name
        self.grades = new_grades

    #Called Methods    
    def average(self):
        return sum(self.grades) / len(self.grades)
        print(self)
    
student1 = Student('Enrio Tequila', [90, 20, 80, 50])
student2 = Student('Enrio Bepis', [90, 50, 80, 88])

#Automaticaly populates self
print(student1.average())
# Same as
print(Student.average(student1))
print(student2.average())


