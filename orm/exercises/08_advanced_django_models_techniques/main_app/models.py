from _pydecimal import Decimal

from django.core import validators
from django.db import models

from main_app.mixins import RechargeEnergyMixin


class Customer(models.Model):
	name = models.CharField(
		max_length=100,
		validators=[
			validators.RegexValidator(regex=r"[a-zA-Z\s]+$", message="Name can only contain letters and spaces"),
		],
	)

	age = models.PositiveIntegerField(
		validators=[
			validators.MinValueValidator(18, message='Age must be greater than 18'),
		]
	)

	email = models.EmailField(
		validators=[
			validators.EmailValidator,
		],
	)

	phone_number = models.CharField(
		max_length=13,
		validators=[
			validators.RegexValidator(regex=r"\+359[0-9]{9}$", message="Phone number must start with a '+359' followed by 9 digits"),
		],
	)

	website_url = models.URLField(
		validators=[
			validators.URLValidator,
		],
	)


class BaseMedia(models.Model):
	title = models.CharField(
		max_length=100,
	)

	description = models.TextField()

	genre = models.CharField(
		max_length=50,
	)

	created_at = models.DateTimeField(
		auto_now_add=True,
	)

	class Meta:
		abstract = True
		ordering = ['-created_at', 'title']


class Book(BaseMedia):
	author = models.CharField(
		max_length=100,
		validators=[
			validators.MinLengthValidator(5, message='Author must be at least 5 characters long'),
		],
	)

	isbn = models.CharField(
		max_length=20,
		validators=[
			validators.MinLengthValidator(6, message='ISBN must be at least 6 characters long'),
		],
	)

	class Meta(BaseMedia.Meta):
		verbose_name = "Model Book"
		verbose_name_plural = "Models of type - Book"


class Movie(BaseMedia):
	director = models.CharField(
		max_length=100,
		validators=[
			validators.MinLengthValidator(8, message='Director must be at least 8 characters long'),
		],
	)

	class Meta(BaseMedia.Meta):
		verbose_name = "Model Movie"
		verbose_name_plural = "Models of type - Movie"


class Music(BaseMedia):
	artist = models.CharField(
		max_length=100,
		validators=[
			validators.MinLengthValidator(9, message='Artist must be at least 9 characters long'),
		],
	)

	class Meta(BaseMedia.Meta):
		verbose_name = "Model Music"
		verbose_name_plural = "Models of type - Music"


class Product(models.Model):
	name = models.CharField(
		max_length=100,
	)

	price = models.DecimalField(
		max_digits=10,
		decimal_places=2,
	)

	def calculate_tax(self) -> float:
		return float(self.price) * 0.08

	def calculate_shipping_cost(self, weight: Decimal) -> float:
		return float(weight) * 2.00

	def format_product_name(self) -> str:
		return f"Product: {self.name}"


class DiscountedProduct(Product):
	class Meta:
		proxy = True

	def calculate_price_without_discount(self):
		return float(self.price) * 1.20

	def calculate_tax(self) -> float:
		return float(self.price) * 0.05

	def calculate_shipping_cost(self, weight: Decimal) -> float:
		return float(weight) * 1.50

	def format_product_name(self) -> str:
		return f"Discounted Product: {self.name}"


class Hero(models.Model, RechargeEnergyMixin):
	name = models.CharField(
		max_length=100,
	)

	hero_title = models.CharField(
		max_length=100,
	)

	energy = models.PositiveIntegerField()


class SpiderHero(Hero):
	class Meta:
		proxy = True

	def swing_from_buildings(self) -> str:
		self.energy -= 80

		if self.energy <= 0:
			return f"{self.name} as Spider Hero is out of web shooter fluid"

		self.save()

		return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):
	class Meta:
		proxy = True

	def run_at_super_speed(self) -> str:
		self.energy -= 65

		if self.energy <= 0:
			return f"{self.name} as Flash Hero needs to recharge the speed force"

		self.save()

		return f"{self.name} as Flash Hero runs at lightning speed, saving the day"


