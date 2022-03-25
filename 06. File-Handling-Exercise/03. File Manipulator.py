import os

while True:
    command = input().split("-")
    if "End" in command:
        break
    task = command[0]
    file_name = command[1]

    if task == "Create":
        with open(file_name, "w") as file:
            pass

    elif task == "Add":
        content = command[2]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif task == "Replace":
        old_content = command[2]
        new_content = command[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as file:
                new = file.read().replace(old_content, new_content)
                file.seek(0)
                file.truncate()
                file.write(new)
        else:
            print("An error occurred")
    elif task == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")