def read_next(*args):
	current_index = -1

	while True:
		try:
			current_index += 1

			for el in args[current_index]:
				yield el
		except IndexError:
			break


for i in read_next("Need", (2, 3), ["words", "."]):
	print(i)
