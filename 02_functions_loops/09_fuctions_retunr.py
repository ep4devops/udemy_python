def i_return():
    return 5 + 5

def i_print():
    print(5 + 5)

result = i_return()
print(result)

another = i_print() # Returns None
print(another)

def fives():
    addition = 5 + 5
    print(addition)
    return addition # stops at return
    print('hello')

