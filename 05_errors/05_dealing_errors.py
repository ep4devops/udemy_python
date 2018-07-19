# Ask for forgiveness, not for permission

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __repr__(self):
        return f'{self.make} {self.model}'
    
class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError('Not a car')
        self.cars.append(car)
    
ford = Garage()
fiesta = Car('Ford', 'Fiesta')
focus = Car('Ford', 'Focus')

# Not Python Philosophy - Ask for permission
#if isinstance(fiesta, Car):
#    ford.add(fiesta)
#else:
#    print('Not a car')

# Python Suggestion: Asking for forgiveness instead
# try to call function, if failed, do something

ford.add_car(fiesta)
ford.add_car(focus)
print(ford.cars)
try:
    ford.add_car('Lol')#
except:
    print('Your car was not a car')