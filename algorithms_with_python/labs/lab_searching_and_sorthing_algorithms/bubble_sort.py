numbers = [int(x) for x in input().split()]

for index in range(len(numbers)):
	for cur_idx in range(len(numbers) - index - 1):
		if numbers[cur_idx] > numbers[cur_idx + 1]:
			numbers[cur_idx], numbers[cur_idx + 1] = numbers[cur_idx + 1], numbers[cur_idx]

print(*numbers, sep=" ")
