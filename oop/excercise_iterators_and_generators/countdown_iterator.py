class countdown_iterator:
	def __init__(self, count: int) -> None:
		self.count = count
		self.current = count

	def __iter__(self):
		return self

	def __next__(self):
		i = self.current

		if i >= 0:
			self.current -= 1

			return i

		else:
			raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
	print(item, end=" ")