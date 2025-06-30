from google.genai import types

from functions.get_file_content import SCHEMA_GET_FILE_CONTENT
from functions.get_files_info import SCHEMA_GET_FILES_INFO
from functions.run_python_file import SCHEMA_RUN_PYTHON_FILE
from functions.write_file import SCHEMA_WRITE_FILE

AVAILABLE_FUNCTIONS = types.Tool(
    function_declarations=[
        SCHEMA_GET_FILES_INFO,
        SCHEMA_GET_FILE_CONTENT,
        SCHEMA_RUN_PYTHON_FILE,
        SCHEMA_WRITE_FILE,
    ]
)


def call_function(function_call_part: types.FunctionCall, verbose: bool = False) -> str:
    """
    Calls a function based on the provided function call part.
    Args:
        function_call_part (types.FunctionCall): The call containing the function name and args.
        verbose (bool): If True, prints the function call details.
    Returns:
        str: The result of the function call.
    """
    if verbose:
        result = (
            f"Calling function: {function_call_part.name}({function_call_part.args})"
        )

    # Simulate calling the function (replace with actual function call logic)
    result = f"Calling function: {function_call_part.name}"

    return result
