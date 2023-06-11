number_of_presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []
total_nice_kids = 0

for row in range(size):
    current_row = list(input().split())
    neighborhood.append(current_row)

    if "S" in current_row:
        santa_pos = [row, current_row.index("S")]

    total_nice_kids += (current_row.count("V"))

nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != "Christmas morning":
    r = santa_pos[0] + directions[command][0]
    c = santa_pos[1] + directions[command][1]

    neighborhood[santa_pos[0]][santa_pos[1]] = "-"  # зануляваме текущата позиция
    current_pos = neighborhood[r][c]
    santa_pos = [r, c]

    if current_pos == "V":
        number_of_presents -= 1
        nice_kids_visited += 1
        neighborhood[r][c] = "-"
    elif current_pos == "C":
        neighborhood[r][c] = "-"

        for value in directions.values():
            cur_r = r + value[0]
            cur_c = c + value[1]

            if neighborhood[cur_r][cur_c] == "V":
                nice_kids_visited += 1
                number_of_presents -= 1
            elif neighborhood[cur_r][cur_c] == "X":
                number_of_presents -= 1

            neighborhood[cur_r][cur_c] = "-"

            if not number_of_presents:
                break

    if not number_of_presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = "S"

if not number_of_presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if nice_kids_visited < total_nice_kids:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
