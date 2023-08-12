from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
	def setUp(self) -> None:
		self.driver = TruckDriver("John", 50.0)

	def test_correct_initialize(self):
		self.assertEqual("John", self.driver.name)
		self.assertEqual(50.0, self.driver.money_per_mile)
		self.assertEqual({}, self.driver.available_cargos)
		self.assertEqual(0.0, self.driver.earned_money)
		self.assertEqual(0, self.driver.miles)

	def test_earned_money_raises_error(self):
		with self.assertRaises(ValueError) as ve:
			self.driver.earned_money -= 100.0

		self.assertEqual("John went bankrupt.", str(ve.exception))

	def test_add_cargo_offer_method_cargo_not_in_available_cargos(self):
		self.driver.available_cargos = {"Sofia": 5, "Vienna": 60}

		actual = self.driver.add_cargo_offer("Varna", 250)
		expected = "Cargo for 250 to Varna was added as an offer."

		self.assertEqual({"Sofia": 5, "Vienna": 60, "Varna": 250}, self.driver.available_cargos)
		self.assertEqual(expected, actual)

	def test_add_cargo_offer_method_already_in_cargos(self):
		self.driver.available_cargos = {"Varna": 5, "Vienna": 60}

		with self.assertRaises(Exception) as ex:
			self.driver.add_cargo_offer("Varna", 250)

		self.assertEqual("Cargo offer is already added.", str(ex.exception))

	def test_drive_best_cargo_offer_with_no_offers_available(self):
		self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())

	def test_drive_best_cargo_offer_with_correct_data(self):
		self.driver.add_cargo_offer("Sofia", 5)
		self.driver.add_cargo_offer("Varna", 10)

		actual = self.driver.drive_best_cargo_offer()

		self.assertEqual(500.0, self.driver.earned_money)
		self.assertEqual(10, self.driver.miles)
		self.assertEqual("John is driving 10 to Varna.", actual)

	def test_check_for_activities_eat_method(self):
		self.driver.earned_money += 100.0
		self.driver.check_for_activities(300)

		self.assertEqual(80.0, self.driver.earned_money)

	def test_check_for_activities_sleep_method(self):
		self.driver.earned_money += 1000.0
		self.driver.check_for_activities(1100)

		self.assertEqual(875.0, self.driver.earned_money)

	def test_check_for_activities_pump_gas_method(self):
		self.driver.earned_money += 1000.0
		self.driver.check_for_activities(1600)

		self.assertEqual(335.0, self.driver.earned_money)

	def test_check_for_activities_repair_truck_method(self):
		self.driver.earned_money += 15000.0
		self.driver.check_for_activities(10001)

		self.assertEqual(3250.0, self.driver.earned_money)

	def test__repr__method(self):
		actual = self.driver.__repr__()
		expected = "John has 0 miles behind his back."

		self.assertEqual(expected, actual)

	def test_bankrupt(self):
		self.driver.money_per_mile = 0.01
		self.driver.add_cargo_offer("California", 2000)

		with self.assertRaises(ValueError) as ve:
			self.driver.drive_best_cargo_offer()

		self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")


if __name__ == "__main__":
	main()
