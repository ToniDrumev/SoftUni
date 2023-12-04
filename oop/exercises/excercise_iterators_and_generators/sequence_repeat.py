class sequence_repeat:
	def __init__(self, sequence: str, number: int) -> None:
		self.sequence = sequence
		self.number = number
		self.string = sequence * number
		self.current_idx = 0

	def __iter__(self):
		return self

	def __next__(self):
		i = self.current_idx

		if i < self.number:
			self.current_idx += 1

			return self.string[i]

		else:
			raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
	print(item, end ='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
	print(item, end ='')
