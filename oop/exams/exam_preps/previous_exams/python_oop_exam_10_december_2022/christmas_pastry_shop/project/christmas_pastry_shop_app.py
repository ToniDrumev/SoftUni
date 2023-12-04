from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
	VALID_DELICACY_TYPES = {
		"Gingerbread": Gingerbread,
		"Stolen": Stolen
	}

	VALID_BOOTH_TYPES = {
		"Open Booth": OpenBooth,
		"Private Booth": PrivateBooth
	}

	def __init__(self):
		self.booths: List[Booth] = []
		self.delicacies: List[Delicacy] = []
		self.income: float = 0.0

	def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
		if self.validadte_by_name(name, self.delicacies):
			raise Exception(f"{name} already exists!")

		if type_delicacy not in self.VALID_DELICACY_TYPES:
			raise Exception(f"{type_delicacy} is not on our delicacy menu!")

		self.delicacies.append(self.VALID_DELICACY_TYPES[type_delicacy](name, price))

		return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

	def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
		if self.validadte_by_number(booth_number, self.booths):
			raise Exception(f"Booth number {booth_number} already exists!")

		if type_booth not in self.VALID_BOOTH_TYPES:
			raise Exception(f"{type_booth} is not a valid booth!")

		self.booths.append(self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity))

		return f"Added booth number {booth_number} in the pastry shop."

	def reserve_booth(self, number_of_people: int) -> str:
		booth = self.find_free_booth(number_of_people, self.booths)

		if not booth:
			raise Exception(f"No available booth for {number_of_people} people!")

		booth.reserve(number_of_people)

		return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

	def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
		booth = self.validadte_by_number(booth_number, self.booths)
		delicacy = self.validadte_by_name(delicacy_name, self.delicacies)

		if not booth:
			raise Exception(f"Could not find booth {booth_number}!")

		if not delicacy:
			raise Exception(f"No {delicacy_name} in the pastry shop!")

		booth.delicacy_orders.append(delicacy)

		return f"Booth {booth_number} ordered {delicacy_name}."

	def leave_booth(self, booth_number: int):
		booth = self.validadte_by_number(booth_number, self.booths)

		bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])
		self.income += bill

		booth.delicacy_orders.clear()
		booth.is_reserved = False
		booth.price_for_reservation = 0

		return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

	def get_income(self):
		return f"Income: {self.income:.2f}lv."

	def validadte_by_name(self, name: str, list_of_obj: list) -> object or None:
		for obj in list_of_obj:
			if obj.name == name:
				return obj

	def validadte_by_number(self, number: str or int, list_of_obj: list) -> object or None:
		for obj in list_of_obj:
			if obj.booth_number == number:
				return obj

	def find_free_booth(self, number_of_people: int, list_of_booths: list) -> Booth or None:
		for booth in list_of_booths:
			if not booth.is_reserved and booth.capacity >= number_of_people:
				return booth


shop = ChristmasPastryShopApp()

print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())

print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))

print(shop.reserve_booth(30))

print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))

print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))

print(shop.get_income())
