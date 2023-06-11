current_row = 1
even_set = set()
odd_set = set()

for _ in range(int(input())):
    name_as_sum = sum([ord(x) for x in input()]) // current_row

    if name_as_sum % 2 == 0:
        even_set.add(name_as_sum)
    else:
        odd_set.add(name_as_sum)

    current_row += 1

if sum(odd_set) == sum(even_set):
    print(*(odd_set & even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*(odd_set - even_set), sep=', ')
else:
    print(*(odd_set ^ even_set), sep=', ')
