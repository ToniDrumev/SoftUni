from typing import List

from project.client import Client
from project.meals.meal import Meal


def is_valid_meal(meal):
	valid_meals = ["Starter", "MainDish", "Dessert"]

	if meal.__class__.__name__ not in valid_meals:
		return False

	return True


class FoodOrdersApp:
	def __init__(self):
		self.menu: List[Meal] = []
		self.clients: List[Client] = []

	def register_client(self, client_phone_number: str):
		for client in self.clients:
			if client.phone_number == client_phone_number:
				raise Exception("The client has already been registered!")

		self.clients.append(Client(client_phone_number))

		return f"Client {client_phone_number} registered successfully."

	def add_meals_to_menu(self, *meals: Meal):
		for meal in meals:
			if not is_valid_meal(meal):
				continue

			self.menu.append(meal)

	def show_menu(self):
		if len(self.menu) < 5:
			return "The menu is not ready!"

		result = []
		for meal in self.menu:
			result.append(meal.details())

		return "\n".join(result)

	def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
		if len(self.menu) < 5:
			raise Exception("The menu is not ready!")

		current_client = None
		for client in self.clients:
			if client.phone_number == client_phone_number:
				current_client = client
				break

		if not current_client:
			current_client = Client(client_phone_number)
			self.clients.append(current_client)

		for name, quantity in meal_names_and_quantities.items():
			for meal in self.menu:
				if meal.name == name:
					if meal.quantity < quantity:
						raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {name}!")

				current_client.shopping_cart.append(name)
				current_client.bill += quantity * meal.price
				self.menu.meal.quantity -= quantity

			else:
				raise Exception(f"{name} is not on the menu!")

		return f"Client {client_phone_number} successfully ordered {', '.join(current_client.shopping_cart)} for {current_client.bill:.2f}lv."

	def cancel_order(self, client_phone_number: str):
		current_client = [c for c in self.clients if c.phone_number == client_phone_number][0]

