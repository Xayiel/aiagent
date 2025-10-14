import os
import subprocess
import sys
from subprocess import CompletedProcess
from google.genai import types

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
        
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes our Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory, the directory in which we are, our Python file that we want to run should be in here. If one isn't provided use '.'.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to our Python file, it should be the whole path including our Python file."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An array/list of optional arguments to pass to our function, they should be strings for our command line interface.",
                items=types.Schema(
                    type=types.Type.STRING
                )
            ),          
        },
        required=["working_directory", "file_path"]
    ),
)