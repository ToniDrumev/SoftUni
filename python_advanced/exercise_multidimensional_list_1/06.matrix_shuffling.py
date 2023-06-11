rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

line = input().split()

while line[0] != "END":
    if len(line) != 5:
        print("Invalid input!")
    else:
        row_1, col_1, row_2, col_2 = [int(x) for x in line[1:]]

        if 0 <= row_1 < rows and 0 <= row_2 < rows and 0 <= col_1 < cols and 0 <= col_2 < cols:
            temporary = matrix[row_1][col_1]
            matrix[row_1][col_1] = matrix[row_2][col_2]
            matrix[row_2][col_2] = temporary
            [print(*row) for row in matrix]
        else:
            print("Invalid input!")

    line = input().split()
