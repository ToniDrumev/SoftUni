from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
	def setUp(self) -> None:
		self.mammal = Mammal("Charlie", "Dog", "Woof!")

	def test_init_of_mammal(self):
		self.assertEqual("Charlie", self.mammal.name)
		self.assertEqual("Dog", self.mammal.type)
		self.assertEqual("Woof!", self.mammal.sound)
		self.assertEqual("animals", self.mammal._Mammal__kingdom)

	def test_make_sound_method(self):
		result = self.mammal.make_sound()

		self.assertEqual("Charlie makes Woof!", result)

	def test_get_kingdom_method(self):
		result = self.mammal.get_kingdom()

		self.assertEqual("animals", result)

	def test_info_method(self):
		result = self.mammal.info()

		self.assertEqual("Charlie is of type Dog", result)


if __name__ == "__main__":
	main()