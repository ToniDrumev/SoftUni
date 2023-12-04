import os
from datetime import timedelta, date
from typing import List

import django
from django.utils.timezone import now

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Car, Owner, Registration


def show_all_authors_with_their_books() -> str:
	authors = Author.objects.all().order_by('id')

	result = []

	for a in authors:
		books = Book.objects.filter(author=a)

		if not books:
			continue

		result.append(f"{a.name} has written - {', '.join(b.title for b in books)}")

	return "\n".join(result)


def delete_all_authors_without_books() -> None:
	Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str) -> None:
	artist = Artist.objects.get(name=artist_name)
	song = Song.objects.get(title=song_title)

	artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> Song:
	artist = Artist.objects.get(name=artist_name)

	return Song.objects.filter(artists=artist).order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
	artist = Artist.objects.get(name=artist_name)
	song = Song.objects.get(title=song_title)

	artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> int:
	product = Product.objects.get(name=product_name)

	return sum(r.rating for r in product.reviews.all()) / product.reviews.count()


def get_reviews_with_high_ratings(threshold: int) -> Review:
	return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> Product:
	return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
	Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates() -> str:
	licenses = DrivingLicense.objects.all().order_by('-id')
	result = []

	for l in licenses:
		result.append(f"License with id: {l.license_number} expires on {l.issue_date + timedelta(days=365)}!")

	return "\n".join(result)


def get_drivers_with_expired_licenses(due_date) -> List[Driver]:
	driving_license = DrivingLicense.objects.all()
	drivers_with_expired_license = []

	for d in driving_license:
		if d.issue_date + timedelta(days=365) > due_date:
			drivers_with_expired_license.append(d.driver)

	return drivers_with_expired_license


def register_car_by_owner(owner: Owner) -> str:
	registration = Registration.objects.filter(car__isnull=True).first()
	car = Car.objects.filter(registration__isnull=True).first()

	car.registration = registration
	car.owner = owner

	car.save()

	registration.car = car
	registration.registration_date = date.today()

	registration.save()

	return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."

