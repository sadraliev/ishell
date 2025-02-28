const fs = require('fs');  // Import the file system module

// Get the directory path from command-line arguments
// If no argument is provided, use the current directory (".")
const directoryPath = process.argv[2] || ".";

// Read the directory content
fs.readdir(directoryPath, (err, files) => {
    if (err) {
        console.error(`Error reading directory: ${err.message}`);
        process.exit(1);  // Exit with an error code
    }

    // Print each file/directory name
    files.forEach(file => {
        console.log(file);
    });
});
