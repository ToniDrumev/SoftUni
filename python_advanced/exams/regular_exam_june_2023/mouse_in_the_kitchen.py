rows, cols = [int(x) for x in input().split(",")]

cupboard_area = []
mouse_pos = []
cheese_count = 0

directions = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1),
}

for row in range(rows):
	line = [x for x in input()]

	cupboard_area.append(line)

	if "M" in line:
		mouse_pos = [row, line.index("M")]

	if "C" in line:
		cheese_count += line.count("C")

command = input()

while command != "danger":
	r = mouse_pos[0] + directions[command][0]
	c = mouse_pos[1] + directions[command][1]

	if not (0 <= r < rows and 0 <= c < cols):
		cupboard_area[mouse_pos[0]][mouse_pos[1]] = "M"
		print("No more cheese for tonight!")
		break

	if cupboard_area[r][c] == "T":
		cupboard_area[r][c] = "M"
		print("Mouse is trapped!")
		break

	if cupboard_area[r][c] == "@":
		command = input()
		continue

	if cupboard_area[r][c] == "C":
		cupboard_area[r][c] = "*"
		cheese_count -= 1

		if cheese_count == 0:
			cupboard_area[r][c] = "M"
			print("Happy mouse! All the cheese is eaten, good night!")
			break

	cupboard_area[mouse_pos[0]][mouse_pos[1]] = "*"

	mouse_pos = [r, c]

	command = input()

else:
	print("Mouse will come back later!")

print("\n". join(["".join(x) for x in cupboard_area]))
