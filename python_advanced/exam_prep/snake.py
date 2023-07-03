size = int(input())

field = []
snake_pos = []
food_eaten = 0

directions = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (1, 0),
}

for row in range(size):
	line = input().split("")

	field.append(line)

	if "S" in line:
		snake_pos = [row, line.index("S")]

while food_eaten < 10:
	direction = input()

	r, c = snake_pos[0], snake_pos[1]

	field[r][c] = "."

	snake_pos = [r + directions[direction][0], c + directions[direction][1]]

	if 0 <= snake_pos[0] < size and 0 <= snake_pos[1] < size:
		break

	if field[snake_pos[0]][snake_pos[1]] == "*":
		food_eaten += 1
