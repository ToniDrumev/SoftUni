from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

	def __init__(self, budget: int):
		self.budget = budget
		self.sponsors = {"Petronas": {1: 1_000_000, 3: 500_000}, "TeamViewer": {5: 100_000, 7: 50_000}}

	def calculate_revenue_after_race(self, race_pos: int) -> str:
		revenue = 0

		for sponsor in self.sponsors:
			for pos in self.sponsors[sponsor]:
				if race_pos <= pos:
					revenue += self.sponsors[sponsor][pos]
					break

		revenue -= 200_000

		self.budget += revenue

		return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
