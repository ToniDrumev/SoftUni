import os

path = os.path.abspath(os.path.curdir)

command = input().split("-")

while command[0] != "End":
    command_name = command[0]
    file_name = os.path.join(path, command[1])

    if command_name == "Create":
        with open(file_name, "w"):
            pass

    elif command_name == "Add":
        file = open(file_name, "a")
        file.write(command[2] + "\n")
        file.close()

    elif command_name == "Replace":
        try:
            with open(file_name, "r+") as file:
                text = file.read()
                text = text.replace(command[2], command[3])

                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print("An error occurred!")

    elif command_name == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred!")

    command = input().split("-")
