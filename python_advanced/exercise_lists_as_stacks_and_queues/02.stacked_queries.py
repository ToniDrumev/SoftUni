from collections import deque

numbers = deque()

n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "1":
        number = int(line[1])
        numbers.append(number)
    elif command == "2":
        if numbers:
            numbers.pop()
    elif command == "3":
        if numbers:
            print(max(numbers))
    elif command == "4":
        if numbers:
            print(min(numbers))

numbers.reverse()

print(*numbers, sep=", ")
