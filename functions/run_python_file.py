import os
import subprocess
import sys
from subprocess import CompletedProcess


def run_python_file(working_directory, file_path, args=[]):
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_full == abs_work or abs_full.startswith(abs_work + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_full):
        return f'Error: File "{file_path}" not found.'
    if not abs_full.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    else:
        try:
            cmd = [sys.executable, abs_full, *args] # assign our interpreter for the program, giving path for our executable and opt args
            completed_process = subprocess.run(cmd, timeout=30, capture_output=True, cwd=abs_work, text=True) 
            if completed_process.returncode != 0:
                return f"Process exited with code {completed_process.returncode}"
            if not isinstance(completed_process, CompletedProcess):
                return f"No output produced"
            else:
                return f"STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr}"
        except Exception as e:
            return f"Error: executing Python file: {e}"