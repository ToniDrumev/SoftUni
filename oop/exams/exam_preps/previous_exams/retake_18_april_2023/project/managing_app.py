from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp():
	def __init__(self):
		self.users: List[User] = []
		self.vehicles: List[BaseVehicle] = []
		self.routes: List[Route] = []

	def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
		user = User(first_name, last_name, driving_license_number)
		users = [x for x in self.users if x.driving_license_number == driving_license_number]

		if users:
			return f"{driving_license_number} has already been registered to our platform."

		self.users.append(user)

		return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

	def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
		if vehicle_type not in ["PassengerCar", "CargoVan"]:
			return f"Vehicle type {vehicle_type} is inaccessible."

		vehicle_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
		vehicle = vehicle_types[vehicle_type](brand, model, license_plate_number)
		vehicles = [x for x in self.vehicles if x.license_plate_number == license_plate_number]

		if vehicles:
			return f"{license_plate_number} belongs to another vehicle."

		self.vehicles.append(vehicle)

		return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

	def allow_route(self, start_point: str, end_point: str, length: float) -> str:
		for route in self.routes:
			if route.start_point == start_point and route.end_point == end_point:
				if route.length == length:
					return f"{start_point}/{end_point} - {length} km had already been added to our platform."

				if route.length < length:
					return f"{start_point}/{end_point} shorter route had already been added to our platform."

				if route.length > length:
					route.is_locked = True

		route = Route(start_point, end_point, length, len(self.routes) + 1)

		self.routes.append(route)

		return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

	def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool) -> str:
		user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
		vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
		route = [r for r in self.routes if r.route_id == route_id][0]

		if user.is_blocked:
			return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

		if vehicle.is_damaged:
			return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

		if route.is_locked:
			return f"Route {route_id} is locked! This trip is not allowed."

		vehicle.drive(route.length)

		if is_accident_happened:
			vehicle.is_damaged = True
			user.decrease_rating()
		else:
			user.increase_rating()

		return str(vehicle)

	def repair_vehicles(self, count: int):
		vehicles_to_repair = [x for x in sorted(self.vehicles, key=lambda x: (x.brand, x.model)) if x.is_damaged]
		counter = 0
		repaired_vehicles = 0

		for v in vehicles_to_repair:
			if counter == count:
				break

			v.is_damaged = False
			v.battery_level = 100
			counter += 1
			repaired_vehicles += 1

		return f"{min(counter, len(vehicles_to_repair))} vehicles were successfully repaired!"

	def users_report(self):
		result = "*** E-Drive-Rent ***\n"

		for user in sorted(self.users, key=lambda x: -x.rating):
			result += str(user) + "\n"

		return result

