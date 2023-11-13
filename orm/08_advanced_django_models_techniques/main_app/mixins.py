class RechargeEnergyMixin:

	def recharge_energy(self, amount: int) -> None:
		recharged_energy = self.energy + amount

		self.energy = recharged_energy if recharged_energy < 100 else 100

		self.save()

