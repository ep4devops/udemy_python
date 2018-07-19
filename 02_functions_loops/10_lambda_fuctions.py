def add_two(x, y):
    return x+y
add_two(10,  5)

(lambda x, y: x+y)(10, 5)

add = lambda x, y: x+y

add(5, 17)

######################

# Higher Order Functions = Accepts functions
def who(data, identify):
    return identify(data)

# First Class Funtion = Can be passed
def my_identifier_funtion(some_data):
    return some_data['name']

user = {'name': 'Jose', 'surname': 'Salvatore'}

# Passing a function
print(who(user, my_identifier_funtion))

# Passing a Lambda
# Hard to understand, but makes some things easier
print(who(user, lambda x: x['name']))


