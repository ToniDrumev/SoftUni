rows, cols = [int(x) for x in input().split()]

for r in range(rows):
    for c in range(cols):
        first = chr(97 + r)
        second = chr(97 + c + r)
        third = chr(97 + r)

        print(first + second + third, end=' ')

    print()
