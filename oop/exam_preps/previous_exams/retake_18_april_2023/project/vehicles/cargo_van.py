from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
	max_mileage = 180.00

	def drive(self, mileage: float) -> None:
		percentage = round(mileage / self.max_mileage * 100)

		self.battery_level -= percentage + 5
