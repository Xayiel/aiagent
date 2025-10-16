import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.get_file_content import schema_get_file_content
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1] if len(sys.argv) > 1 else None
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
messages = [
    types.Content( # message object, see it as a container for our message conversation, knows who send the message and what the message is
        role="user", # tells our ai its user input      
        parts=[types.Part(text=user_prompt)] # creates a list of "parts", in this case just a text part for the AI to process
        ),
]

def main():
    # Call generate_content 20 times, with try-except block, keep going until response.txt is returned or 20 iterations.
    count = 20
    try:
        while count != 0:
            available_functions = types.Tool(
                function_declarations=[
                    schema_get_files_info,
                    schema_get_file_content,
                    schema_run_python_file,
                    schema_write_file
                ]
            )
            config = types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", 
                contents=messages, 
                config=config
            )
            # Check candidates property of response, a list of response variations(usually1). Should contain "i want to call get_files_info", add it to our 
            # conversation. Iterate over each candidate and add its .content to your messages list.
            for candidate in response.candidates:
                messages.append(candidate.content)
                
            verbose = "--verbose" in sys.argv
            if response.function_calls:
                for function_call in response.function_calls:
                    result = call_function(function_call, verbose=verbose)
                    # check if result exists
                    if result is None:
                        raise Exception("No result from function call")
                    # check if parts is present and not empty
                    if result.parts is None or len(result.parts) <= 0:
                        raise Exception("Missing parts in the function call result")
                    # check function_response exists
                    parts_ob = result.parts[0] # parts[0] is a types.Part object which contains an attribute of function_response object.
                    if parts_ob.function_response is None:
                        raise Exception("Missing function response in result")
                    # check if response exists
                    if parts_ob.function_response.response is None:
                        raise Exception("Missing function_response.response in result")
                    if verbose:
                        print(f"-> {parts_ob.function_response.response}")
                    # After each function call, use types.Content to convert function_responses into a message with a role of "user" and append it to messages.
                    converted_function_call = types.Content(
                        role="user",
                        parts=result.parts
                    )
                    messages.append(converted_function_call)
            elif hasattr(response, "text"):
                print(response.text)
                break
            else:
                print("Error: Model didn't return function calls or text")
                break
            count -= 1    
            if count == 0:
                print("The loop has finished.") 
    except Exception as e:
        print(f"Error: {e}")
    # usage = response.usage_metadata

if __name__ == "__main__":
    main()
