from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
	def setUp(self) -> None:
		self.car = SecondHandCar("Tesla", "electric", 100_000, 100_000.0)

	def test_correct_initialization(self):
		self.assertEqual("Tesla", self.car.model)
		self.assertEqual("electric", self.car.car_type)
		self.assertEqual(100_000, self.car.mileage)
		self.assertEqual(100_000.0, self.car.price)
		self.assertEqual([], self.car.repairs)

	def test_lower_price(self):
		with self.assertRaises(ValueError) as ve:
			self.car.price = 0.9

		self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

	def test_lower_mileage(self):
		with self.assertRaises(ValueError) as ve:
			self.car.mileage = 100

		self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

	def test_set_promotional_price_raise_error(self):
		with self.assertRaises(ValueError) as ve:
			self.car.set_promotional_price(100_001)

		self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

	def test_set_promotional_price_correctly(self):
		result = self.car.set_promotional_price(100)

		self.assertEqual(100, self.car.price)
		self.assertEqual("The promotional price has been successfully set.", result)

	def test_need_repair_price_is_high(self):
		result = self.car.need_repair(50_001, "asd")

		self.assertEqual("Repair is impossible!", result)

	def test_need_repair_successfull(self):
		result = self.car.need_repair(100, "asd")

		self.assertEqual(100_100, self.car.price)
		self.assertEqual(["asd"], self.car.repairs)
		self.assertEqual("Price has been increased due to repair charges.", result)

	def test__gt__method_diff_types(self):
		other_car = SecondHandCar("test", "test", 1000, 1000.0)

		result = self.car > other_car

		self.assertEqual("Cars cannot be compared. Type mismatch!", result)

	def test__gt__method_correct(self):
		other_car = SecondHandCar("test", "electric", 1000, 1000.0)

		result = self.car > other_car

		self.assertEqual(True, result)

	def test__str__method(self):
		expected = """Model Tesla | Type electric | Milage 100000km
Current price: 100000.00 | Number of Repairs: 0"""
		actual = str(self.car)

		self.assertEqual(expected, actual)