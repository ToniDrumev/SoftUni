class Customer:
	ID = 1

	def __init__(self, name: str, address: str, email: str) -> None:
		self.name = name
		self.address = address
		self.email = email
		self.id = Customer.ID

		Customer.ID += 1

	@staticmethod
	def get_next_id() -> int:
		return Customer.ID

	def __repr__(self) -> str:
		return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
