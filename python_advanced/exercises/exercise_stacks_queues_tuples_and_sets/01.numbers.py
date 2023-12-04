first_set_of_numbers = set(int(x) for x in input().split())
second_set_of_numbers = set(int(x) for x in input().split())

map_functions = {
    "Add First": lambda x: first_set_of_numbers.update(command_numbers),
    "Add Second": lambda x: second_set_of_numbers.update(command_numbers),
    "Remove First": lambda x: first_set_of_numbers.difference_update(command_numbers),
    "Remove Second": lambda x: second_set_of_numbers.difference_update(command_numbers),
    "Check Subset": lambda x: print("False") if not first_set_of_numbers.issubset(
        second_set_of_numbers) and not second_set_of_numbers.issubset(first_set_of_numbers) else print("True")
}

for _ in range(int(input())):
    command_args = input().split()

    command = " ".join(command_args[0:2])
    command_numbers = set(int(x) for x in command_args[2:])

    map_functions[command](command_numbers)

print(*first_set_of_numbers, sep=", ")
print(*second_set_of_numbers, sep=", ")
