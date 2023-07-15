from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

	def make_sound(self):
		return "Hoot Hoot"

	@property
	def weight_gain(self):
		return 0.25

	@property
	def food_eating(self):
		return [Meat]


class Hen(Bird):

	def make_sound(self):
		return "Cluck"

	@property
	def weight_gain(self):
		return 0.35

	@property
	def food_eating(self):
		return [Meat, Vegetable, Fruit, Seed]
