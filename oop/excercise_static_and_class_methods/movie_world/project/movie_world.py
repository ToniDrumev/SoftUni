from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
	def __init__(self, name: str):
		self.name = name
		self.customers: List[Customer] = []
		self.dvds: List[DVD] = []

	@staticmethod
	def dvd_capacity():
		return 15

	@staticmethod
	def customer_capacity():
		return 10

	def add_customer(self, customer: Customer) -> None:
		if not len(self.customers) == self.customer_capacity():
			self.customers.append(customer)

	def add_dvd(self, dvd: DVD) -> None:
		if not len(self.dvds) == self.dvd_capacity():
			self.dvds.append(dvd)

	def rent_dvd(self, customer_id: int, dvd_id: int):
		c = [c for c in self.customers if c.id == customer_id][0]
		d = [d for d in self.dvds if d.id == dvd_id][0]

		if d.age_restriction > c.age:
			return f"{c.name} should be at least {d.age_restriction} to rent this movie"

		if d in c.rented_dvds:
			return f"{c.name} has already rented {d.name}"

		elif d.is_rented:
			return "DVD is already rented"

		d.is_rented = True
		c.rented_dvds.append(d)
		return f"{c.name} has successfully rented {d.name}"

	def return_dvd(self, customer_id, dvd_id):
		c = [c for c in self.customers if c.id == customer_id][0]
		d = [d for d in self.dvds if d.id == dvd_id][0]

		if d not in c.rented_dvds:
			return f"{c.name} does not have that DVD"

		d.is_rented = False
		c.rented_dvds.remove(d)

		return f"{c.name} has successfully returned {d.name}"

	def __repr__(self) -> str:
		res = ""

		for c in self.customers:
			res += f"{c}\n"

		for d in self.dvds:
			res += f"{d}\n"

		return res

