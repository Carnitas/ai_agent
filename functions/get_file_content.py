import os

MAX_CHARS = 10000


def get_file_content(working_directory: str, file_path: str) -> str:
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f"File not found or is not a regular file: {file_path}"
    with open(abs_file_path, encoding="utf-8") as file:
        content = file.read(MAX_CHARS)
    if len(content) > 10000:
        return content + f"[...File {file_path} truncated at 10000 characters]"
    return content
