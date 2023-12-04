from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
	def setUp(self) -> None:
		self.tennis_player = TennisPlayer("Rafael Nadal", 30, 100.0)

	def test_correct_initialization(self):
		self.assertEqual("Rafael Nadal", self.tennis_player.name)
		self.assertEqual(30, self.tennis_player.age)
		self.assertEqual(100.0, self.tennis_player.points)
		self.assertEqual([], self.tennis_player.wins)

	def test_name_shorter_than_two_raises_error(self):
		with self.assertRaises(ValueError) as ve:
			self.tennis_player.name = "as"

		self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

	def test_age_less_than_18(self):
		with self.assertRaises(ValueError) as ve:
			self.tennis_player.age = 17

		self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

	def test_add_new_win_correctly(self):
		self.tennis_player.add_new_win("Wimbeldon")

		self.assertEqual("Wimbeldon", self.tennis_player.wins[0])

	def test_add_new_win_tournament_already_won(self):
		self.tennis_player.add_new_win("Wimbeldon")
		actual = self.tennis_player.add_new_win("Wimbeldon")

		self.assertEqual("Wimbeldon has been already added to the list of wins!", actual)

	def test_less_than_method(self):
		other = TennisPlayer("Novak Jokovic", 28, 150.0)

		result = self.tennis_player < other

		self.assertEqual("Novak Jokovic is a top seeded player and he/she is better than Rafael Nadal", result)

		self.tennis_player.points += 100.0

		result = self.tennis_player < other

		self.assertEqual("Rafael Nadal is a better player than Novak Jokovic", result)

	def test__str__method(self):
		self.tennis_player.add_new_win("Wimbeldon")
		self.tennis_player.add_new_win("Rolan Garos")

		actual = str(self.tennis_player)

		expected = "Tennis Player: Rafael Nadal\n" \
               "Age: 30\n" \
               "Points: 100.0\n" \
               "Tournaments won: Wimbeldon, Rolan Garos"

		self.assertEqual(expected, actual)

if __name__ == "__main__":
	main()