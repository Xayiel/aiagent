import os

def get_files_info(working_directory, directory="."):
    abs_work = os.path.abspath(working_directory) # Get the absolute path to our working directory.
    abs_dir = os.path.abspath(os.path.join(working_directory, directory)) # Get the absolute path and append our paths

    if not (abs_dir == abs_work or abs_dir.startswith(abs_work + os.sep)): # We add sep to avoid false matches(check notes)
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_dir):
        return f'Error: "{directory}" is not a directory'
    else:
        try:
            items = os.listdir(abs_dir)
        except Exception as e:
            return f"Error: {e}"
        lines = []
        for name in items:
            entry = os.path.join(abs_dir, name)
            try:
                size = os.path.getsize(entry) 
                is_dir = os.path.isdir(entry)
                lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
            except Exception as e:
                lines.append(f"- {name}: Error: {e}")
    return "\n".join(lines)

