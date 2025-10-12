import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_work = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_work == abs_filepath or abs_filepath.startswith(abs_work + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)