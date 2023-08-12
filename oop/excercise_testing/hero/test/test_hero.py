from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

	def setUp(self) -> None:
		self.hero = Hero("Some name", 1, 75.0, 100.0)
		self.enemy_hero = Hero("Other name", 1, 50.0, 75.0)

	def test_correct_initialize_method(self):
		self.assertEqual("Some name", self.hero.username)
		self.assertEqual(1, self.hero.level)
		self.assertEqual(75.0, self.hero.health)
		self.assertEqual(100.0, self.hero.damage)

		self.assertIsInstance(self.hero.username, str)
		self.assertIsInstance(self.hero.level, int)
		self.assertIsInstance(self.hero.health, float)
		self.assertIsInstance(self.hero.damage, float)

	def test_battle_method_cant_fight_yourself(self):
		self.enemy_hero.username = "Some name"
		with self.assertRaises(Exception) as ex:
			self.hero.battle(self.enemy_hero)

		self.assertEqual("You cannot fight yourself", str(ex.exception))

	def test_battle_method_own_health_lt_zero(self):
		self.hero.health = -1
		with self.assertRaises(ValueError) as ve:
			self.hero.battle(self.enemy_hero)

		expected = "Your health is lower than or equal to 0. You need to rest"
		actual = str(ve.exception)

		self.assertEqual(expected, actual)

	def test_battle_method_enemy_health_lt_zero(self):
		self.enemy_hero.health = 0

		with self.assertRaises(ValueError) as ve:
			self.hero.battle(self.enemy_hero)

		expected = "You cannot fight Other name. He needs to rest"
		actual = str(ve.exception)

		self.assertEqual(expected, actual)

	def test_battle_method_draw_result(self):

		expected = "Draw"
		actual = self.hero.battle(self.enemy_hero)

		self.assertEqual(0, self.hero.health)
		self.assertEqual(-50, self.enemy_hero.health)
		self.assertEqual(expected, actual)

	def test_battle_method_hero_win(self):
		self.enemy_hero.damage = 0

		expected = "You win"
		actual = self.hero.battle(self.enemy_hero)

		self.assertEqual(2, self.hero.level)
		self.assertEqual(80.0, self.hero.health)
		self.assertEqual(105.0, self.hero.damage)
		self.assertEqual(expected, actual)

		# self.hero.level = 11
		# self.hero.health = 104.0
		# self.hero.damage = 35.0
		#
		# self.enemy_hero = Hero("Other name", 1, 100.0, 30.0)
		#
		# expected = "You win"
		# actual = self.hero.battle(self.enemy_hero)
		#
		# self.assertEqual(expected, actual)

	def test_battle_method_enemy_hero_win(self):
		self.hero.damage = 0

		expected = "You lose"
		actual = self.hero.battle(self.enemy_hero)

		self.assertEqual(2, self.enemy_hero.level)
		self.assertEqual(55.0, self.enemy_hero.health)
		self.assertEqual(80.0, self.enemy_hero.damage)
		self.assertEqual(expected, actual)

		# self.enemy_hero.level = 11
		# self.enemy_hero.health = 104.0
		# self.enemy_hero.damage = 35.0
		#
		# self.hero = Hero("Some name", 1, 100.0, 30.0)
		#
		# expected = "You lose"
		# actual = self.hero.battle(self.enemy_hero)
		#
		# self.assertEqual(expected, actual)

	def test_str_method_check(self):
		expected = "Hero Some name: 1 lvl\n" \
				   "Health: 75.0\n" \
				   "Damage: 100.0\n"

		actual = str(self.hero)

		self.assertEqual(expected, actual)


if __name__ == "__main__":
	main()
