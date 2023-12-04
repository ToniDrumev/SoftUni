class AreasFound:
	def __init__(self, row, col, size):
		self.row = row
		self.col = col
		self.size = size


def find_area(row, col, matrix):
	if row >= len(matrix) or row < 0 or col < 0 or col >= len(matrix[0]):
		return 0

	if matrix[row][col] == "*":
		return 0

	if matrix[row][col] == "v":
		return 0

	matrix[row][col] = "v"

	result = 1

	result += find_area(row + 1, col, matrix)  # Down
	result += find_area(row - 1, col, matrix)  # Up
	result += find_area(row, col + 1, matrix)  # Right
	result += find_area(row, col - 1, matrix)  # Left

	return result


rows = int(input())
cols = int(input())
matrix = []

[matrix.append(list(input())) for _ in range(rows)]

areas = []
for row in range(rows):
	for col in range(cols):
		size = find_area(row, col, matrix)

		if size == 0:
			continue

		areas.append(AreasFound(row, col, size))

print(f"Total areas found: {len(areas)}")
for idx, a in enumerate(sorted(areas, key=lambda a: -a.size)):
	print(f"Area #{idx + 1} at ({a.row}, {a.col}), size: {a.size}")

