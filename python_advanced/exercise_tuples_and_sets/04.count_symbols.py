from collections import deque

text = deque([x for x in input()])

symbols = {}

while text:
    char = text.pop()
    if char not in symbols:
        symbols[char] = 0

    symbols[char] += 1

for key, value in sorted(symbols.items()):
    print(f"{key}: {value} time/s")
    
