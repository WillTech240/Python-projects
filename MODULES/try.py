import os
import sys
import getpass

password = getpass.getpass("Enter your password: ")
print("You entered:", "*" * len(password))

python_project = r"C:\Users\USER\Documents\Python projects"
dir_name, file_name = os.path.split(python_project)
print("Directory:", dir_name)
print("File name:", file_name)

print("1. Python version:", sys.version)
print("Python version info:", sys.version_info)
print()

print("2. Command-line arguments (sys.argv):", sys.argv)
print("Number of arguments:", len(sys.argv))
print()
print("All command-line arguments:", sys.argv)
print("Script name:", sys.argv[0])

print("3. Module search path (sys.path):")
for path in sys.path:
    print(" -", path)





