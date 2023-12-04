from project.movie_app import MovieApp
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action
from project.movie_specification.movie import Movie
from project.movie_specification.thriller import Thriller
from project.user import User

m = MovieApp()

print(m.register_user("Pesho", 18))
print(m.register_user("Pesho", 21))

user = User("asd", 25)
movie1 = Action("action1", 1999, m.users_collection[0])
movie2 = Fantasy("fantasy1", 2003, m.users_collection[1])
movie3 = Thriller("thril1", 2015, m.users_collection[1])

print(m.upload_movie(m.users_collection[0].username, movie1))
m.upload_movie(m.users_collection[1].username, movie2)

print(m.edit_movie("Gosho", movie2, title="fan2", year=2000))

print(m.like_movie("Pesho", movie3))
print(m.like_movie("Pesho", movie2))

print(m.display_movies())

print(m)

