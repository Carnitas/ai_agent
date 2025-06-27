import os

from google.genai import types

from llm.config import MAX_CHARS


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


SCHEMA_GET_FILE_CONTENT = types.FunctionDeclaration(
    name="get_file_content",
    description="Prints the contents of a file to the console, "
    "constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to read, relative to the working directory.",
            ),
        },
    ),
)
