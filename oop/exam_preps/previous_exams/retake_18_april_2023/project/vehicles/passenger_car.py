from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
	max_mileage = 450.00

	def drive(self, mileage: float) -> None:
		percentage = round(mileage / self.max_mileage * 100)

		self.battery_level -= percentage
