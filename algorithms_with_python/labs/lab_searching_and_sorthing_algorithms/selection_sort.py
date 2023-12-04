numbers = [int(x) for x in input().split()]

for idx in range(len(numbers)):
	min_idx = idx

	for cur_idx in range(idx + 1, len(numbers)):
		if numbers[cur_idx] < numbers[min_idx]:
			min_idx = cur_idx

	numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

print(*numbers, sep=" ")
