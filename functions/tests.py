from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content

def main():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("\nResult for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    print("\nResult for '../' directory:")
    print(get_files_info("calculator", "../"))
# def main():
#     print("Result for current directory:")
#     print(get_file_content("calculator", "main.py"))

#     print("\nResult for 'pkg' directory:")
#     print(get_file_content("calculator", "pkg/calculator.py"))

#     print("\nResult for '/bin' directory:")
#     print(get_file_content("calculator", "/bin/cat"))

#     print("\nResult for '../' directory:")
#     print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()
