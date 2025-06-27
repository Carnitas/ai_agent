import os

from google.genai import types


def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}", it is outside the allowed working directory'
    with open(abs_file_path, "w", encoding="utf-8") as file:
        file.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


SCHEMA_WRITE_FILE = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the provided content, "
    "constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)
