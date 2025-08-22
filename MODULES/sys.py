# sys_module_demo.py

import sys

print("SYS MODULE DEMO\n")

# 1. Python version
print("1. Python version:", sys.version)
print("Python version info:", sys.version_info)
print()

# 2. Command-line arguments
# Example: python sys_module_demo.py arg1 arg2
print("2. Command-line arguments (sys.argv):", sys.argv)
print("Number of arguments:", len(sys.argv))
print()

# 3. Module search path
print("3. Module search path (sys.path):")
for path in sys.path:
    print(" -", path)
print()

# 4. Platform info
print("4. Platform:", sys.platform)
print()

# 5. System exit
# Uncomment the next line to test sys.exit (it will stop the program)
# sys.exit("Exiting the program with a message.")

# 6. Standard streams
print("6. Standard output (sys.stdout) example:")
print("Hello to standard output!")

print("Standard error (sys.stderr) example:")
sys.stderr.write("This is an error message!\n")
print()

# 7. Get recursion limit
print("7. Current recursion limit:", sys.getrecursionlimit())

# 8. Set recursion limit (use carefully!)
# sys.setrecursionlimit(2000)
# print("Updated recursion limit:", sys.getrecursionlimit())
