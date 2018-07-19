numbers = list(range(10))

# List Calculation
doubled_numbers = [n*2 for n in numbers]
print(doubled_numbers)

phrases = [f'I am {age} years old' for age in doubled_numbers]
print(phrases)

names = ['Joe', 'Rolf', 'Anne']
lowercase_names = [name.lower() for name in names]
print(lowercase_names)

# With conditionals
even = [n for n in range(10) if n % 2 == 0]
print(even)

names = ['joe', 'Rolf', 'Anne']
guests = ['Joe', 'Rolf', 'Muhammend']

friends_party = [names.capitalize() for names in names if names in guests ]
print(friends_party)