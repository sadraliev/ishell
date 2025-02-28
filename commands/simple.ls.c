#include <stdio.h>   // For printf() and perror()
#include <dirent.h>  // For directory functions: opendir(), readdir(), closedir()

int main(int argc, char *argv[]) {
    struct dirent *entry;  // Structure to store directory entries
    DIR *dir;              // Pointer to a directory stream

    // Determine the directory to list
    // If an argument is provided, use it as the directory path
    // Otherwise, use the current directory (".")
    char *path = (argc > 1) ? argv[1] : ".";

    // Open the specified directory
    dir = opendir(path);
    if (dir == NULL) {  // Check for errors
        perror("opendir");  // Print error message if directory cannot be opened
        return 1;  // Exit with error code
    }

    // Read and print each entry in the directory
    while ((entry = readdir(dir)) != NULL) {
        printf("%s\n", entry->d_name);  // Print the filename
    }

    // Close the directory stream
    closedir(dir);
    return 0;  // Exit successfully
}
