import os
import subprocess

from google.genai import types


def run_python_file(working_directory: str, file_path: str) -> str:
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}", it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if os.path.splitext(abs_file_path)[1] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python3", abs_file_path],
            check=False,
            cwd=working_directory,
            timeout=30,
            capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"

    stdout_str = result.stdout.decode("utf-8").strip()
    stderr_str = result.stderr.decode("utf-8").strip()

    if not stdout_str and not stderr_str:
        return "Error: No output produced."

    output = f"STDOUT: {stdout_str}\nSTDERR: {stderr_str}"
    if result.returncode:
        output += f"\nProcess exited with code {result.returncode}"
    return output


SCHEMA_RUN_PYTHON_FILE = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional arguments, "
    "limited to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the Python file to execute, "
                "relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to pass to the Python file.",
            ),
        },
    ),
)
