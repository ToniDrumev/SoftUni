from project.product import Product


class Drink(Product):
	def __init__(self, name: str) -> None:
		super(Drink, self).__init__(name, quantity=10)
