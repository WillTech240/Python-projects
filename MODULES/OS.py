#Getting the current working directory

#Listing files and directories

#Creating, renaming, and deleting folders

#File path operations (join, exists, isfile, isdir)

#Getting OS info and environment variables

#Running system commands

#Extra path operations (abspath, split, getsize)

# os_module_demo.py

import os

print("OS MODULE DEMO\n")

# 1. Current Working Directory
print("1. Current directory:", os.getcwd())

# 2. List files and directories
print("2. List of files and folders:", os.listdir())

# 3. Create a new folder
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"3. '{folder_name}' created")
else:
    print(f"3. '{folder_name}' already exists")

print("Current files/folders after mkdir:", os.listdir())

# 4. Rename the folder
new_name = "renamed_folder"
if os.path.exists(folder_name):
    os.rename(folder_name, new_name)
    print(f"4. Folder renamed to '{new_name}'")

print("Current files/folders after rename:", os.listdir())

# 5. Remove the folder
if os.path.exists(new_name):
    os.rmdir(new_name)
    print(f"5. '{new_name}' removed")

print("Current files/folders after rmdir:", os.listdir())

# 6. File path operations
file_path = "example.txt"

# Join paths
full_path = os.path.join(os.getcwd(), file_path)
print("\n6. Full path to file:", full_path)

# Check existence
print("Does the file exist?", os.path.exists(file_path))

# Check if it is a file or directory
print("Is it a file?", os.path.isfile(file_path))
print("Is it a directory?", os.path.isdir(os.getcwd()))

# 7. OS info and environment
import os
import getpass  # safer way to get current username

# OS name
print("\n7. OS Name:", os.name)  # 'nt' for Windows, 'posix' for Linux/Mac

# Get login username safely
try:
    username = os.getlogin()
except OSError:
    # fallback if os.getlogin() fails
    username = getpass.getuser()
print("Login user:", username)

# PATH environment variable
print("PATH environment variable:", os.environ.get("PATH"))

# 8. Running system commands
print("\n8. Running system command:")
os.system("echo Hello from OS module!")          # Works on both Windows/Linux (for Windows use 'echo', Linux can use 'ls')

# 9. Extra useful examples
print("\n9. Extra examples:")

# Get absolute path
print("Absolute path of current directory:", os.path.abspath("."))

# Split path
dir_name, file_name = os.path.split(full_path)
print("Directory:", dir_name)
print("File name:", file_name)

# Get file size (if exists)
if os.path.exists(file_path):
    print("File size:", os.path.getsize(file_path), "bytes")
else:
    print(f"'{file_path}' does not exist, so size cannot be determined")
