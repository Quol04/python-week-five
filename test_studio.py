from movie import Movie
from studio import Studio   

stud=Studio("Testing the Studio")
stud.add_movie(Movie("The Godfather", "Francis Ford Coppola", 2000))
stud.add_movie(Movie("The Dark Knight", "Christopher Nolan", 2008))
stud.add_movie(Movie("Pulp Fiction", "Quentin Tarantino", 1994))
stud.add_movie(Movie("Schindler's List", "Steven Spielberg", 1993))

print("Studio Catalog:")
for movie in stud.get_movies():
    print("\n", movie)

# print(stud.get_movies())


   