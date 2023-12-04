unique_usernames = set()

for _ in range(int(input())):
    unique_usernames.add(input())

print(*unique_usernames, sep='\n')

