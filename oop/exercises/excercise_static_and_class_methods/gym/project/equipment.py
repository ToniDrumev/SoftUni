class Equipment:
	ID = 1

	def __init__(self, name: str) -> None:
		self.name = name
		self.id = Equipment.ID

		Equipment.ID += 1

	@staticmethod
	def get_next_id() -> int:
		return Equipment.ID

	def __repr__(self) -> str:
		return f"Equipment <{self.id}> {self.name}"

