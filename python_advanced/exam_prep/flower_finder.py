from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {
    "rose": set("rose"),
    "tulip": set("tulip"),
    "lotus": set("lotus"),
    "daffodil": set("daffodil")
}

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower, value in flowers.items():
        if vowel in value:
            flowers[flower].discard(vowel)
        if consonant in flower:
            flowers[flower].discard(consonant)

        if not flowers[flower]:
            print(f"Word found: {flower}")
            break
    else:
        continue

    break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '. join(vowels)}")

if consonants:
    print(f"Consonants left: {' '. join(consonants)}")
