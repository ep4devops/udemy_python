friends = {'rolf', 'anna', 'charlie'}
guests = {'jose', 'rolf', 'ruth', 'charlie'}

present_firends = friends & guests

print(present_firends)


names = ['Rolf', 'Anna', 'Charly']
time_last_seen = [10, 15, 8]

firends_last_seen = {names[i]: time_last_seen[i] for i in range(len(names))}
print(firends_last_seen)

# Zip Give a list of tuples
# Dict turns Tuples into Key Value Pairs
firends_last_seen = dict(zip(names, time_last_seen))
print(firends_last_seen)

