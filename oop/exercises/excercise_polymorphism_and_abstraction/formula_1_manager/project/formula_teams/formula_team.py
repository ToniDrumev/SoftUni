from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):

	@abstractmethod
	def __init__(self, budget: int) -> None:
		self.budget = budget
		self.sponsors: Dict[str: Dict[int: int]] = {}

	@property
	def budget(self):
		return self.__budget

	@budget.setter
	def budget(self, value):
		if value < 1_000_000:
			raise ValueError("F1 is an expensive sport, find more sponsors!")

		self.__budget = value

	@abstractmethod
	def calculate_revenue_after_race(self, race_pos: int):
		...
