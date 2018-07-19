class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = Student('Rolf', 'MIT')
rolf.marks.append(78)
rolf.marks.append(88)

print(rolf.average())


class Foo:
    @classmethod
    # cls is the Value of the class holding it
    # cls is convention
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()
Foo.hi()

class Bar:
    @staticmethod
    #
    def hi():
        print('Hello I dont take parameters')

Bar.hi()