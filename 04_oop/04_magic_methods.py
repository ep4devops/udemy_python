class Student:
    # Is called automatically when new Object created
    def __init__(self, name):
        self.name = name

movies = ['Matrix', 'Finding Nemo']
# All are Classes
print(movies.__class__)
print('String'.__class__)
print(len(movies))

class Garage:
    def __init__(self):
        self.cars = []
    # Len Function
    def __len__(self):
        return len(self.cars)
    # Indexing Function
    def __getitem__(self, i):
        return self.cars[i]
    # Description
    def __repr__(self):
        return f'<Garage {self.cars}>'
    # User oriented descripton
    def __str__(self):
        return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

# Len FUnction __len__
print(len(ford))

# Indexing Function __getitem__
print(ford[0])

# Iteration needs len and getitem
for cars in ford:
    print(cars)

#NEeds __repr__ or __str__
print(ford)

