import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_work = os.path.abspath(working_directory)
    abs_fullpath = os.path.abspath(os.path.join(working_directory, file_path))
    parent = os.path.dirname(abs_fullpath) # Get directory portion of our full path

    if not (abs_fullpath == abs_work or abs_fullpath.startswith(abs_work + os.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(parent): # Makes directory if our directory path doesn't exist.
        try:
            os.makedirs(parent, exist_ok=True) # Silently succeed if dir already exists, creates missing parents
        except Exception as e:
            return f"Error: {e}"
    else:
        try:
            with open(abs_fullpath, "w") as f: # will create new file if one doesn't exist
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f"Error: {e}"                                                                             
        
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes our content into specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory, the directory in which we are, our Python file that we want to run should be in here."
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Should be the file we want to write to or overwrite, if it doesn't exist it will create a new file."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="A string of content provided by the user, which we will use to write to our given file."
            ),
        },
        required=["working_directory", "file_path", "content"]
    ),
)