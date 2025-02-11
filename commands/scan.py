#!/usr/bin/env python3
import os
import sys
import stat
import time

# Define icons for different types
FOLDER_ICON = "📂"
FILE_ICON = "📄"
EXEC_ICON = "🔧"
HIDDEN_ICON = "👻"

# Define ANSI colors
DIR_COLOR = "\033[1;34m"     # Blue for directories
FILE_COLOR = "\033[1;37m"    # White (bold) for regular files
EXEC_COLOR = "\033[1;32m"    # Green for executables
HIDDEN_COLOR = "\033[1;35m"  # Magenta for hidden files
RESET_COLOR = "\033[0m"      # Reset color to default

def get_icon_and_color(item_path):
    """Return an appropriate icon and color based on the file type."""
    if os.path.isdir(item_path):
        return FOLDER_ICON, DIR_COLOR
    elif os.access(item_path, os.X_OK):  # Executable files
        return EXEC_ICON, EXEC_COLOR
    elif item_path.startswith("."):
        return HIDDEN_ICON, HIDDEN_COLOR
    else:
        return FILE_ICON, FILE_COLOR

def list_files(path=".", show_all=False, long_format=False):
    try:
        items = os.listdir(path)
        
        # Sort items alphabetically
        items.sort()

        # Filter out hidden files unless `-a` is used
        if not show_all:
            items = [item for item in items if not item.startswith(".")]

        for item in items:
            item_path = os.path.join(path, item)
            icon, color = get_icon_and_color(item_path)

            if long_format:
                # Get file stats
                file_stat = os.stat(item_path)
                permissions = stat.filemode(file_stat.st_mode)
                size = file_stat.st_size
                mtime = time.strftime("%b %d %H:%M", time.localtime(file_stat.st_mtime))
                
                # Print details with color and icon
                print(f"{permissions} {size:8} {mtime} {color}{icon} {item}{'/' if os.path.isdir(item_path) else ''}{RESET_COLOR}")
            else:
                print(f"{color}{icon} {item}/" if os.path.isdir(item_path) else f"{color}{icon} {item}{RESET_COLOR}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def main():
    show_all = "-a" in sys.argv
    long_format = "-l" in sys.argv
    path = "."

    # Check if a custom directory is provided
    for arg in sys.argv[1:]:
        if not arg.startswith("-"):
            path = arg
            break

    list_files(path, show_all, long_format)
    print(RESET_COLOR)

if __name__ == "__main__":
    main()
