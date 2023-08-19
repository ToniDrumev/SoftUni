def nested_loops_with_recursion(num, vector, index):
	if index == len(vector):
		print(" ".join(vector))
		return

	for n in range(1, num + 1):
		vector[index] = str(n)
		nested_loops_with_recursion(num, vector, index + 1)


number = int(input())
vector = [None for _ in range(number)]

nested_loops_with_recursion(number, vector, 0)
