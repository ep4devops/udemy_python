"""
Enter 'a' to add a movie, 
'l' to see your movies,
'f' to find a movie,
'q' to quit

-- add movies
-- see movies
-- find a movie
-- stop running the programm

Tasks
[x] Decide where to store movies
[x] Show interface and recieve input
[] Allow users to add movies
[] Show all their movies
[] Find a movie
[x] Stop running
"""

movies = []

"""
movie = {
    'name' = (str)
    'director' = (str)
    'year' = (int)
}
"""

def menu():
    user_input = 0
    while user_input != 'q':
        user_input = input("What do you want to do? ")
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            list_movies()
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            print('Quitting Programm ...')
        else:
            print('Unknown programm - try again')


def add_movie():
    correct = 'n'
    while correct != 'y':
        name = input("Enter the name: ")
        director = input("Enter the Director")
        year = int(input("Enter the Year:" ))
        correct = input(f'Name: {name}\nDirector: {director}\nYear: {year}\ncorrect? (y/n): ')
    movies.append({
        'name' : name, 
        'director': director, 
        'year': year
    })

def list_movies():
    for i in movies:
        print(i)

def find_movie():
    search = input("What to find? ")
    for i in movies[:]:
        if search == i['name']:
                print(i)
        elif search == i['director']:
                print(i)
        elif int(search) == i['year']:
                print(i)        
movies.append({'name': 'Matrix', 'director': 'enrico', 'year': 1994})
menu()
        

