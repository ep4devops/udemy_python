set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

#Intersection - Schnittmenger / Inner Join
print(set_one.intersection(set_two))
print(set_one & set_two)


#Union - Combined without duplicates
print(set_one.union(set_two))
print(set_one | set_two)


#Difference / Outer Join
print(set_one.difference(set_two))
print(set_one - set_two)



