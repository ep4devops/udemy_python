# Without OOP

my_student = {
    'name': 'Rolf',
    'grades': [70, 80, 90, 99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])
    #j = 0
    #for i in student['grades']:
    #   j+=i
    #return j / len(student['grades'])

print(average_grade(my_student))

# Problem tightly coupled 

# OOP

