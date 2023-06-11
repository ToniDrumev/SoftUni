from collections import deque

special_symbols = {"-", ",", ".", "!", "?"}

file = open("text.txt", "r")

text = file.readlines()

for idx in range(len(text)):
    if idx % 2 == 0:
        line = text[idx]

        for ch in line:
            if ch in special_symbols:
                line = line.replace(ch, "@")

        current_line = deque(line.split())
        reversed_line = deque()

        while current_line:
            reversed_line.append(current_line.pop())

        print(" ".join(reversed_line))

file.close()
