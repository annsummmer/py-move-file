import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return
    command_name, file_to_move, path = parts

    if command_name != "mv":
        return

    if not os.path.isfile(file_to_move):
        return

    folder_path = os.path.dirname(path)

    if folder_path:
        os.makedirs(folder_path, exist_ok=True)

    os.rename(file_to_move, path)
