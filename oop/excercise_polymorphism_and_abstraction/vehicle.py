from abc import ABC, abstractmethod


class Vehicle(ABC):
	def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
		self.fuel_quantity = fuel_quantity
		self.fuel_consumption = fuel_consumption

	@abstractmethod
	def drive(self):
		...

	@abstractmethod
	def refuel(self):
		...


class Car(Vehicle):

	def drive(self, distance: int) -> None:
		fuel_needed = (self.fuel_consumption + 0.9) * distance

		if fuel_needed <= self.fuel_quantity:
			self.fuel_quantity -= fuel_needed

	def refuel(self, fuel) -> None:
		self.fuel_quantity += fuel


class Truck(Vehicle):

	def drive(self, distance: int) -> None:
		fuel_needed = (self.fuel_consumption + 1.6) * distance

		if fuel_needed <= self.fuel_quantity:
			self.fuel_quantity -= fuel_needed

	def refuel(self, fuel) -> None:
		self.fuel_quantity += fuel * 0.95


car = Car(20, 5)

car.drive(3)
print(car.fuel_quantity)

car.refuel(10)
print(car.fuel_quantity)