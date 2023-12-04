from typing import List
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
	def __init__(self):
		self.movies_collection: List[Movie] = []
		self.users_collection: List[User] = []

	def register_user(self, username: str, age: int) -> str:
		user = User(username, age)

		cur_user = [u for u in self.users_collection if u.username == username]

		if cur_user:
			raise Exception("User already exists!")

		self.users_collection.append(user)

		return f"{username} registered successfully."

	def upload_movie(self, username: str, movie: Movie) -> str:
		cur_user = None
		for user in self.users_collection:
			if user.username == username:
				cur_user = user
				break

		if not cur_user:
			raise Exception("This user does not exist!")

		if movie.owner.username != cur_user.username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		if movie in self.movies_collection:
			raise Exception("Movie already added to the collection!")

		cur_user.movies_owned.append(movie)
		self.movies_collection.append(movie)

		return f"{username} successfully added {movie.title} movie."

	def edit_movie(self, username: str, movie: Movie, **movie_attributes) -> str:
		cur_user = None
		for user in self.users_collection:
			if user.username == username:
				cur_user = user
				break

		if movie not in self.movies_collection:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		if movie.owner.username != cur_user.username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		for key, value in movie_attributes.items():
			setattr(movie, key, value)

		return f"{username} successfully edited {movie.title} movie."

	def delete_movie(self, username: str, movie: Movie) -> str:
		cur_user = None
		for user in self.users_collection:
			if user.username == username:
				cur_user = user
				break

		if movie not in self.movies_collection:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		if movie.owner.username != cur_user.username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		cur_user.movies_owned.remove(movie)
		self.movies_collection.remove(movie)

		return f"{username} successfully deleted {movie.title} movie."

	def like_movie(self, username: str, movie: Movie) -> str:
		cur_user = None
		for user in self.users_collection:
			if user.username == username:
				cur_user = user
				break

		if movie.owner.username == cur_user.username:
			raise Exception(f"{username} is the owner of the movie {movie.title}!")

		if movie in cur_user.movies_liked:
			raise Exception(f"{username} already liked the movie {movie.title}!")

		movie.likes += 1
		cur_user.movies_liked.append(movie)

		return f"{username} liked {movie.title} movie."

	def dislike_movie(self, username: str, movie: Movie) -> str:
		cur_user = None
		for user in self.users_collection:
			if user.username == username:
				cur_user = user
				break

		if movie not in cur_user.movies_liked:
			raise Exception(f"{username} has not liked the movie {movie.title}!")

		movie.likes -= 1
		cur_user.movies_liked.remove(movie)

		return f"{username} disliked {movie.title} movie."

	def display_movies(self) -> str:
		return ("\n".join(x.details() for x in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))))\
			if self.movies_collection \
			else "No movies found."

		# result = "\n".join(x.details() for x in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

		# return result

	def __str__(self) -> str:
		return f"All users: {(', '.join(x.username for x in self.users_collection)) if self.users_collection else 'No users.'}" + \
				f"\nAll movies: {(', '.join(x.title for x in self.movies_collection)) if self.movies_collection else 'No movies.'}"
