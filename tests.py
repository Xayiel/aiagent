#from functions.get_files_info import get_files_info

# def main():
#     print("Result for current directory:")
#     print(get_files_info("calculator", "."))

#     print("\nResult for 'pkg' directory:")
#     print(get_files_info("calculator", "pkg"))

#     print("\nResult for '/bin' directory:")
#     print(get_files_info("calculator", "/bin"))

#     print("\nResult for '../' directory:")
#     print(get_files_info("calculator", "../"))

# from functions.get_file_content import get_file_content

# def main():
#     # print(get_file_content("calculator", "lorem.txt"))
#     print("Result for current directory:")
#     print(get_file_content("calculator", "main.py"))

#     print("\nResult for 'pkg' directory:")
#     print(get_file_content("calculator", "pkg/calculator.py"))

#     print("\nResult for '/bin' directory:")
#     print(get_file_content("calculator", "/bin/cat"))

#     print("\nResult for '../' directory:")
#     print(get_file_content("calculator", "pkg/does_not_exist.py"))

# from functions.write_file import write_file

# def main():
#     print("Result for current directory:")
#     print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

#     print("\nResult for current directory:")
#     print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

#     print("\nResult for current directory:")
#     print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

from functions.run_python_file import run_python_file

def main():
    print("1. Result for main.py, should print instructions")
    print(run_python_file("calculator", "main.py"))

    print("\n2. Result for main.py, [3 + 5], should return calculator")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\n3. Result for tests.py")
    print(run_python_file("calculator", "tests.py"))

    print("\n4. Results for ../main.py, should error")
    print(run_python_file("calculator", "../main.py"))

    print("\n5. Result for nonexis.py, should error")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\n6. Result for lorem.txt, should error")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
