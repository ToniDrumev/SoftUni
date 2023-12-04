import os
import django
from django.db.models import Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None) -> str:
	directors = []

	if search_name and search_nationality:
		directors.append(
			f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
			for d in Director.objects.filter(
				full_name__icontains=search_name, nationality__icontains=search_nationality
			).order_by('full_name'))

	elif search_name:
		directors.append(
			f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
			for d in Director.objects.filter(
				full_name__icontains=search_name
			).order_by('full_name'))

	elif search_nationality:
		directors.append(
			f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
			for d in Director.objects.filter(
				nationality__icontains=search_nationality
			).order_by('full_name'))

	else:
		return ""

	return "\n".join(*directors)


def get_top_director() -> str:
	director = Director.objects.get_directors_by_movies_count().first()
	movies = Movie.objects.filter(director=director)

	if not director:
		return ""

	return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor() -> str:
	actor = Actor.objects.annotate(count_movies=Count('actor_movies')).order_by('-count_movies', 'full_name').first()
	movies = None
	avg_rating = 0

	if not actor:
		return ""

	if actor:
		movies = Movie.objects.filter(starring_actor=actor)

		if not movies:
			return ""

		if movies:
			avg_rating = sum(m.rating for m in movies) / len(movies)

	return (f"Top Actor: {actor.full_name}, starring in movies: {', '.join(m.title for m in movies)}"
			f", movies average rating: {avg_rating:.1f}")


def get_actors_by_movies_count():

	actors = Actor.objects.annotate(
		movies_counter=Count('movie')
	).order_by('-movies_counter', 'full_name')[:3]

	if not actors or not Movie.objects.all():
		return ""

	actors_by_movies = []

	for actor in actors:
		actors_by_movies.append(f"{actor.full_name}, participated in {actor.movies_counter} movies")

	return "\n".join(actors_by_movies)


def get_top_rated_awarded_movie() -> str:
	movie = Movie.objects.select_related(
		'starring_actor'
	).prefetch_related(
		'actors'
	).filter(
		is_awarded=True
	).order_by('-rating', 'title').first()

	if not movie:
		return ""

	starring_actor = movie.starring_actor.full_name if movie.starring_actor else "N/A"

	cast = ', '.join([a.full_name for a in movie.actors.order_by('full_name')])

	return (f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}. Starring actor: {starring_actor}. Cast: {cast}.")


def increase_rating():
	movies = Movie.objects.filter(is_classic=True, rating__lt=10.0)

	if not movies:
		return "No ratings increased."

	for movie in movies:
		movie.rating = F('rating') + 0.1
		movie.save()

	return f"Rating increased for {len(movies)} movies."

