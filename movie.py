# 1. Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# 2. Add attributes and methods to bring the class to life!
# 3. Use constructors to initialize each object with unique values.
# 4. Add an inheritance layer to explore polymorphism or encapsulation.

# Create a class representing a Movie
class Movie:
    def __init__(self, title, director, release_year,):
        self.title = title
        self.director = director
        self.release_year = release_year
       

    def get_movie_info(self):
        return f"{self.title} was released in '{self.release_year}' - Directed by {self.director}"

   