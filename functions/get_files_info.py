import os

from google.genai import types


def get_files_info(working_directory: str, directory: str | None) -> list[str] | str:
    if directory is None:
        directory = working_directory
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    if not abs_directory.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    file_info: list[str] = []
    for file in os.listdir(abs_directory):
        file_path = os.path.join(abs_directory, file)
        file_size = os.path.getsize(file_path)
        file_info.append(
            f"- {file}: file_size={file_size} bytes, is_dir={os.path.isdir(file_path)}"
        )
    return "\n".join(file_info) if file_info else "No files found in the directory."


SCHEMA_GET_FILES_INFO = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, "
    "constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. "
                "If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
