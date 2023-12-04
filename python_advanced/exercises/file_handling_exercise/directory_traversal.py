import os

files = os.listdir()

extensions = {}
result = []

try:
    for file in files:
        if os.path.isfile(file):
            filename, extension = file.split(".")

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

except FileNotFoundError:
    print("No such directory!")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, filenames in extensions:
    result.append(f".{extension}")
    [result.append(f"- - - {filename}") for filename in filenames]

with open("report.txt", "w") as file:
    file.write("\n".join(result))
