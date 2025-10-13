import os

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
            with open(abs_fullpath, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f"Error: {e}"                                                                             