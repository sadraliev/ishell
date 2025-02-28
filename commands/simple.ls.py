import os   # Import the operating system module
import sys  # Import the system module to handle command-line arguments

# Get the directory path from command-line arguments
# If no argument is provided, use the current directory (".")
directory_path = sys.argv[1] if len(sys.argv) > 1 else "."

try:
    # List all files and directories in the specified directory
    files = os.listdir(directory_path)

    # Print each file/directory name
    for file in files:
        print(file)

except FileNotFoundError:
    print(f"Error: Directory '{directory_path}' not found.")
    sys.exit(1)  # Exit with an error code
except PermissionError:
    print(f"Error: Permission denied for '{directory_path}'.")
    sys.exit(1)
