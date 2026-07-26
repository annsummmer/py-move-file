import os

def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return
    command_name, file_to_move, path = parts

    if command_name != "mv":
        return

    home_dir = os.getcwd()
    content = ""

    with open(file_to_move, "r") as src:
        content = src.read()

    elems = path.split("/")
    folder_path = elems[:-1]
    file_name = elems[-1]

    for i, key in enumerate(folder_path):
        if not os.path.isdir(key):
            os.mkdir(key)
        os.chdir(key)

    with open(file_name, "w") as f:
        f.write(content)

    os.chdir(home_dir)
    os.remove(file_to_move)
