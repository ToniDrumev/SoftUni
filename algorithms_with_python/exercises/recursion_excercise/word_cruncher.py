def find_all_sol(index, target_string, words_by_index, words_count, solution):
	if index >= len(target_string):
		print(" ".join(solution))
		return

	if index not in words_by_index:
		return

	for word in words_by_index[index]:
		if words_count[word] == 0:
			continue

		solution.append(word)
		words_count[word] -= 1

		find_all_sol(index + len(word), target_string, words_by_index, words_count, solution)

		solution.pop()
		words_count[word] += 1


strings = input().split(", ")
target_string = input()

words_by_index = {}
words_count = {}

for word in strings:
	if word in words_count:
		words_count[word] += 1
		continue

	words_count[word] = 1

	index = 0
	try:
		while True:
			index = target_string.index(word, index)

			if index not in words_by_index:
				words_by_index[index] = []

			words_by_index[index].append(word)
			index += len(word)

	except ValueError:
		pass


find_all_sol(0, target_string, words_by_index, words_count, [])
