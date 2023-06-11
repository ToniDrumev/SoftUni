sequence = [sub.split() for sub in input().split("|")]

print(*([' '.join(x) for x in sequence[::-1] if x]))
