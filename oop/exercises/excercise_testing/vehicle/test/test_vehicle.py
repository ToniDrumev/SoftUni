from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

	def setUp(self) -> None:
		self.vehicle = Vehicle(15.5, 50.0)

	def test_check_correct_initialize_method(self):
		capacity = self.vehicle.fuel

		self.assertEqual(15.5, self.vehicle.fuel)
		self.assertEqual(15.5, capacity)
		self.assertEqual(50.0, self.vehicle.horse_power)
		self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

	def test_check_correct_initialize_data(self):
		self.assertIsInstance(self.vehicle.fuel, float)
		self.assertIsInstance(self.vehicle.capacity, float)
		self.assertIsInstance(self.vehicle.fuel_consumption, float)
		self.assertIsInstance(self.vehicle.horse_power, float)

	def test_check_for_negative_or_zero_values(self):
		self.assertGreater(self.vehicle.fuel, 0)
		self.assertGreater(self.vehicle.horse_power, 0)

	def test_check_drive_method_raise_ex(self):
		with self.assertRaises(Exception) as ex:
			self.vehicle.drive(150)

		self.assertEqual("Not enough fuel", str(ex.exception))

	def test_check_drive_method_works(self):

		self.assertEqual(15.5, self.vehicle.fuel)

		self.vehicle.drive(10)
		result = self.vehicle.fuel_consumption * 10

		self.assertEqual(15.5 - result, self.vehicle.fuel)

	def test_try_to_refuel_more_than_capacity(self):
		with self.assertRaises(Exception) as ex:
			self.vehicle.refuel(100)

		self.assertEqual("Too much fuel", str(ex.exception))

	def test_refuel_with_less_quantity(self):
		self.assertEqual(15.5, self.vehicle.fuel)

		self.vehicle.drive(10)
		self.assertEqual(3, self.vehicle.fuel)

		result = self.vehicle.fuel + 10
		self.vehicle.refuel(10)

		self.assertEqual(result, self.vehicle.fuel)

	def test_check_str_method(self):
		expected = "The vehicle has 50.0 horse power with 15.5 fuel left and 1.25 fuel consumption"
		actual = str(self.vehicle)

		self.assertEqual(expected, actual)

		self.vehicle.drive(10)

		expected = "The vehicle has 50.0 horse power with 3.0 fuel left and 1.25 fuel consumption"
		actual = str(self.vehicle)

		self.assertEqual(expected, actual)


if __name__ == "__main__":
	main()
