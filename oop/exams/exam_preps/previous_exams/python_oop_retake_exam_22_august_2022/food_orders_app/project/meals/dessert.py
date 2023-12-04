from project.meals.meal import Meal


class Dessert(Meal):
	def __init__(self, name: str, price: float, quantity: int):
		super().__init__(name, price, 30)

	def details(self):
		return f"Dessert {self.name}: {self.price}lv/piece"
