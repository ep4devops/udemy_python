my_variable = 'hello'
greetings = 'nice to meet you'

friend = 'enrico'

my_list = ['hello', 'hi', 'nice to meet you']
my_tuble = ('hello', 'hi', 'nice to meet you')
my_set = {'hello', 'hi', 'nice to meet you'}

print(my_list)
print(my_tuble)
print(my_set)


'''
List
- mutable

Tuple
- immutable

Set 
- no order
- unique items
 
'''


my_short_tuple = ('hello')
# No Tuple  because considered as a mathematicel operation
print(my_short_tuple)
my_short_tuple2 = ('hello',)
print(my_short_tuple2)
# Comma is tuple
my_short_tuple3 = 'hello',
print(my_short_tuple3)

# called a subscript
# 0 = erstes element
print(my_list[0])
print(my_tuble[0])
#does not work for sets

#Append List
my_list.append('llalalala')

#Apppent Tuple
my_tuble = my_tuble + ('bla',)
print(my_tuble)

#Add Set (unique)
my_set.add('hello')
print(my_set)