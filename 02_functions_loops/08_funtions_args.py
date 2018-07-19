name = input('Enter your name: ')

def greeting(name):
    return 'Hello, ' + name

print(greeting(name))


#Broken
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} is not prime')
            break
    print(f'{number} is prime')

is_prime(10)