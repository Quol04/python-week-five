from movie import Movie

class Studio:
    def __init__(self, name):
        ## Initialize the studio with a name and an empty list of movies
        self.name = name
        self.movies = []

    def add_movie(self,mov):
        ## Add a movie to the studio's list of movies
        self.movies.append(mov)

    def get_movies(self):
        ## Return the list of movies in the studio
        return [movie.get_movie_info() for movie in self.movies]



    
