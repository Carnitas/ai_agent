import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}", it is outside the allowed working directory'
    with open(abs_file_path, "w", encoding="utf-8") as file:
        file.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
