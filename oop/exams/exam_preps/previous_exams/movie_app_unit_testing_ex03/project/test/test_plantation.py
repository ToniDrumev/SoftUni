from unittest import TestCase
from project.plantation import Plantation


class TestPlantation(TestCase):

	def setUp(self) -> None:
		self.plantation = Plantation(10)

	def test_check_initialization_success(self):
		self.assertEqual(10, self.plantation.size)
		self.assertEqual({}, self.plantation.plants)
		self.assertEqual([], self.plantation.workers)

	def test_types_of_init_method(self):
		self.assertIsInstance(self.plantation.size, int)
		self.assertIsInstance(self.plantation.plants, dict)
		self.assertIsInstance(self.plantation.workers, list)

	def test_size_setter_if_value_less_than_zero(self):
		with self.assertRaises(ValueError) as ve:
			self.plantation.size = -3

		self.assertEqual("Size must be positive number!", str(ve.exception))

	def test_worker_method_with_worker_already_hired(self):
		self.plantation.hire_worker("Pesho")

		with self.assertRaises(ValueError) as ve:
			self.plantation.hire_worker("Pesho")

		self.assertEqual("Worker already hired!", str(ve.exception))

	def test_worker_method_successfully_add_worker(self):
		result = self.plantation.hire_worker("Pesho")
		result2 = self.plantation.hire_worker("Gosho")

		self.assertEqual(["Pesho", "Gosho"], self.plantation.workers)
		self.assertEqual("Pesho successfully hired.", result)
		self.assertEqual("Gosho successfully hired.", result2)

	def test_len_method(self):
		self.plantation.plants["Pesho"] = [2, 3]
		self.plantation.plants["Gosho"] = [3, 7, 8]

		result = len(self.plantation)

		self.assertEqual(5, result)

	def test_planting_method_worker_not_hired(self):
		with self.assertRaises(ValueError) as ve:
			self.plantation.planting("Pesho", "apple")

		self.assertEqual("Worker with name Pesho is not hired!", str(ve.exception))

	def test_planting_method_plantation_full(self):
		self.plantation.hire_worker("Pesho")
		self.plantation.hire_worker("Gosho")
		self.plantation.plants["Pesho"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

		with self.assertRaises(ValueError) as ve:
			self.plantation.planting("Pesho", "apple")

		self.assertEqual("The plantation is full!", str(ve.exception))

	def test_planting_method_successfully_planting_worker_already_planted(self):
		self.plantation.hire_worker("Pesho")

		self.plantation.planting("Pesho", "apple")
		result = self.plantation.planting("Pesho", "banana")

		self.assertEqual(["apple", "banana"], self.plantation.plants["Pesho"])
		self.assertEqual("Pesho planted banana.", result)

	def test_planting_method_successfully_planting_for_first_time(self):
		self.plantation.hire_worker("Pesho")

		result = self.plantation.planting("Pesho", "apple")

		self.assertEqual(["apple"], self.plantation.plants["Pesho"])
		self.assertEqual("Pesho planted it's first apple.", result)


	def test__str__method(self):
		self.plantation.hire_worker("Pesho")
		self.plantation.hire_worker("Gosho")

		self.plantation.planting("Pesho", "apple")
		self.plantation.planting("Pesho", "banana")
		self.plantation.planting("Gosho", "pear")

		expected = "Plantation size: 10\nPesho, Gosho\nPesho planted: apple, banana\nGosho planted: pear"
		actual = str(self.plantation)

		self.assertEqual(expected, actual)

	def test__repr__method(self):
		self.plantation.hire_worker("Pesho")
		self.plantation.hire_worker("Gosho")

		self.plantation.planting("Pesho", "apple")
		self.plantation.planting("Pesho", "banana")
		self.plantation.planting("Gosho", "pear")

		expected = "Size: 10\nWorkers: Pesho, Gosho"
		actual = repr(self.plantation)

		self.assertEqual(expected, actual)
