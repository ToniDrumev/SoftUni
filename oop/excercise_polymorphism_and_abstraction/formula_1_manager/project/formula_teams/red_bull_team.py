from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

	def __init__(self, budget: int):
		self.budget = budget
		self.sponsors = {"Oracle": {1: 1_500_000, 2: 800_000}, "Honda": {8: 20_000, 10: 10_000}}

	def calculate_revenue_after_race(self, race_pos: int) -> str:
		revenue = 0

		for sponsor in self.sponsors:
			for pos in self.sponsors[sponsor]:
				if race_pos <= pos:
					revenue += self.sponsors[sponsor][pos]
					break

		revenue -= 250_000

		self.budget += revenue

		return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
