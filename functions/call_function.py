from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False): # function call part is a types.FunctionCall has .name and .args property
    print(f"Calling function: {function_call_part.name}({function_call_part.args})") if verbose is True else print(f" - Calling function: {function_call_part.name}")
    function_name = function_call_part.name
    function_args = function_call_part.args.copy()
    function_args["working_directory"] = "./calculator"
    function_map = {"get_file_content":get_file_content, "get_files_info":get_files_info, "run_python_file":run_python_file, "write_file":write_file}
    func = function_map.get(function_name)

    if func is None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}",}
                )
            ],
        )
    else:
        function_result = func(**function_args)
        return types.Content(
            role="tool",                                                                                                    
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )

    


