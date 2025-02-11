# Creating Your Own Shell Command in Linux

This guide will walk you through the basics of creating your own custom shell command in Linux. By the end, you'll be able to create a simple command, make it executable, and use it from anywhere in the terminal.
---
## 📌 Step 1: Write a Script
First, create a script file. You can use Python, Node.js, Bash, or any other scripting language.

### Example: Creating a Python Command
1. Open a terminal and create a new script file:
```sh
vim mycommand.py
```
2. Add the following Python code to the file:
```python
#!/usr/bin/env python3
import sys

def main():
    # Read input from stdin
    input_text = sys.stdin.read().strip()
    
    # Modify input
    output_text = f"{input_text} - Processed by mycommand"
    
    # Print output
    print(output_text)

if __name__ == "__main__":
    main()
```
2. Save the file (CTRL + X, then Y, then ENTER).
## 📌 Step 2: Make the Script Executable
To run the script as a command, it needs execution permissions.

Run the following command:

```sh
chmod +x mycommand.py
```
Now, you can execute it like this:

```sh
python ./mycommand.py
```
However, this only works if you're in the same directory. Let's move it to a system-wide location.

## 📌 Step 3: Move the Script to a System Directory
To use your script from anywhere, move it to `/usr/local/bin`, which is in your system's `$PATH`.

Run:

```sh
sudo mv mycommand.py /usr/local/bin/mycommand
// or
sudo cp mycommand.py /usr/local/bin/mycommand
```
Now, you can use it as a normal shell command:

```sh
echo "Hello, world" | mycommand
```
Expected Output:

```sh
Hello, world - Processed by mycommand
```
## 📌 Step 4: Verify Your Command (Optional)
To check if your command is available system-wide, run:

```sh
which mycommand
```
If it returns:
```sh
/usr/local/bin/mycommand
```
That means your command is successfully installed! 🚀

## 📌 Step 5: Testing Your Command with Pipes
Since we created a command that processes input, you can pipe output from another command into it:

```sh
ls | mycommand
```
🎉 Congratulations! You've created your own custom shell command!

## 🎯 Summary

| Step | Command                                           | Description                      |
|------|---------------------------------------------------|----------------------------------|
| 1    | `nano mycommand.py`                               | Create a script file             |
| 2    | `chmod +x mycommand.py`                           | Make it executable               |
| 3    | `sudo mv mycommand.py /usr/local/bin/mycommand`   | Move to system directory         |
| 4    | `mycommand`                                       | Run it from anywhere             |
| 5    | `echo "Hello" \| mycommand`                        | Test the command with a pipe     |


#### 🎯 Bonus: Examples in folder /commands