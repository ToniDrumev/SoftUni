from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
	VALID_SERVICE_TYPES = {
		"MainService": MainService,
		"SecondaryService": SecondaryService
	}

	VALID_ROBOT_TYPES = {
		"MaleRobot": MaleRobot,
		"FemaleRobot": FemaleRobot,
	}

	def __init__(self):
		self.robots: List[BaseRobot] = []
		self.services: List[BaseService] = []

	def add_service(self, service_type: str, name: str) -> str:
		if service_type not in self.VALID_SERVICE_TYPES.keys():
			raise Exception("Invalid service type!")

		self.services.append(self.VALID_SERVICE_TYPES[service_type](name))

		return f"{service_type} is successfully added."

	def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
		if robot_type not in self.VALID_ROBOT_TYPES.keys():
			raise Exception("Invalid robot type!")

		self.robots.append(self.VALID_ROBOT_TYPES[robot_type](name, kind, price))

		return f"{robot_type} is successfully added."

	def validate_robot(self, robot_name: str, robots_list: List[BaseRobot]) -> BaseRobot or None:
		for robot in robots_list:
			if robot.name == robot_name:
				return robot

	def validate_service(self, service_name: str, service_list: List[BaseService]) -> BaseService or None:
		for service in service_list:
			if service.name == service_name:
				return service

	def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
		current_robot = self.validate_robot(robot_name, self.robots)
		current_service = self.validate_service(service_name, self.services)

		if current_robot.__class__.__name__ == "FemaleRobot" and current_service.__class__.__name__ == "MainService" or \
			current_robot.__class__.__name__ == "MaleRobot" and current_service.__class__.__name__ == "SecondaryService":

			return "Unsuitable service."

		if len(current_service.robots) >= current_service.capacity:
			raise Exception("Not enough capacity for this robot!")

		self.robots.remove(current_robot)
		current_service.robots.append(current_robot)

		return f"Successfully added {robot_name} to {service_name}."

	def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:

		service = self.validate_service(service_name, self.services)
		current_robot = self.validate_robot(robot_name, service.robots)

		if not current_robot:
			raise Exception("No such robot in this service!")

		service.robots.remove(current_robot)
		self.robots.append(current_robot)

		return f"Successfully removed {robot_name} from {service_name}."

	def feed_all_robots_from_service(self, service_name: str) -> str:
		service = self.validate_service(service_name, self.services)

		for r in service.robots:
			r.eating()

		return f"Robots fed: {len(service.robots)}."

	def service_price(self, service_name: str) -> str:
		service = self.validate_service(service_name, self.services)

		total_price = 0

		for r in service.robots:
			total_price += r.price

		return f"The value of service {service_name} is {total_price:.2f}."

	def __str__(self):
		result = ""

		result += "\n".join([service.details() for service in self.services])

		return result


m = RobotsManagingApp()

print(m.add_robot("FemaleRobot", "Penka", "nice", 100))
print(m.add_robot("MaleRobot", "Pesho", "nice", 100))

m.add_service("SecondaryService", "asd")

print(m.add_robot_to_service("Penka", "asd"))
a = 5