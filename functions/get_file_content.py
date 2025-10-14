import os
from functions.config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_work = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_work == abs_filepath or abs_filepath.startswith(abs_work + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        try:
            with open(abs_filepath, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if f.read(1) !=  "": # We can check if there's still more chars left and if there is announce we truncated.
                    return f'{file_content_string} [...File "{file_path}" truncated at 10000 characters]'
        except Exception as e:
            return f"Error: {e}"
        return f'{file_content_string}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the contents of the given file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory to use as the base path. Use '.' for the current directory if not specified by the user.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to our Python file, it should be the whole path including our Python file."
            ),
        },
    ), 
)