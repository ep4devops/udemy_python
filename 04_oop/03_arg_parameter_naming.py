class Movie:
    def __init__(self, name, year):
        # Two distinct variables
        self.name = name
        self.year = year

print(Movie('Matrix', '1994').name)
movie = Movie('Matrix', '1994')
print(movie.name)

