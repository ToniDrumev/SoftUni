import os
from string import punctuation

path_to_file = os.path.abspath("text.txt")

with open(path_to_file, "r") as file:
    text = file.readlines()

output = open("output.txt", "w")

for idx in range(len(text)):
    letters = 0
    punct_marks = 0

    for symbol in text[idx]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punct_marks += 1

    output.write(f"Line {idx + 1}: {''.join(text[idx][:-1])} ({letters})({punct_marks})\n")

output.close()