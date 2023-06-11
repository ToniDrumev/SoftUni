rows, cols = [int(x) for x in input().split()]

text = [x for x in input()]
sequence = text

matrix = []

for r in range(rows):
    if len(sequence) < cols:
        sequence.extend(text)

    cut_piece = sequence[:cols]
    sequence = sequence[cols:]

    if r % 2 == 0:
        matrix.append(cut_piece)
    else:
        matrix.append(cut_piece[::-1])

    print(*matrix[r], sep='')