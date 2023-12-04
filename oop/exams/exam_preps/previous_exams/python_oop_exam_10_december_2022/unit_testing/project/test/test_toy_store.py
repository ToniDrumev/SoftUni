from unittest import TestCase

from project.toy_store import ToyStore


class TestToyStore(TestCase):
	def setUp(self) -> None:
		self.store = ToyStore()

	def test_correct_initialization(self):
		self.assertEqual({
			"A": None,
			"B": None,
			"C": None,
			"D": None,
			"E": None,
			"G": None,
			"F": None,
		}, self.store.toy_shelf)

	def test_add_toy_shelf_not_in_shelves(self):
		with self.assertRaises(Exception) as ex:
			self.store.add_toy("z", "test")

		self.assertEqual("Shelf doesn't exist!", str(ex.exception))

	def test_add_toy_toy_already_on_shelf(self):
		self.store.toy_shelf["A"] = "test"

		with self.assertRaises(Exception) as ex:
			self.store.add_toy("A", "test")

		self.assertEqual("Toy is already in shelf!", str(ex.exception))

	def test_add_toy_shelf_already_taken(self):
		self.store.toy_shelf["A"] = "test"

		with self.assertRaises(Exception) as ex:
			self.store.add_toy("A", "test2")

		self.assertEqual("Shelf is already taken!", str(ex.exception))

	def test_add_toy_correctly(self):
		result = self.store.add_toy("A", "test")

		self.assertEqual("test", self.store.toy_shelf["A"])
		self.assertEqual("Toy:test placed successfully!", result)

	def test_remove_toy_shelf_not_listed(self):
		with self.assertRaises(Exception) as ex:
			self.store.remove_toy("z", "test")

		self.assertEqual("Shelf doesn't exist!", str(ex.exception))

	def test_remove_toy_toy_not_on_that_shelf(self):
		self.store.add_toy("A", "test")

		with self.assertRaises(Exception) as ex:
			self.store.remove_toy("A", "test2")

		self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

	def test_remove_toy_correctly(self):
		self.store.add_toy("A", "test")

		result = self.store.remove_toy("A", "test")

		self.assertEqual(None, self.store.toy_shelf["A"])
		self.assertEqual("Remove toy:test successfully!", result)


