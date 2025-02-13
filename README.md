## Table of Contents
- [Creating Your Own Shell Command in Linux](#creating-your-own-shell-command-in-linux)
  - [This guide will walk you through the basics of creating your own custom shell command in Linux. By the end, you'll be able to create a simple command, make it executable, and use it from anywhere in the terminal.](#this-guide-will-walk-you-through-the-basics-of-creating-your-own-custom-shell-command-in-linux-by-the-end-youll-be-able-to-create-a-simple-command-make-it-executable-and-use-it-from-anywhere-in-the-terminal)
  - [📌 Step 1: Write a Script](#-step-1-write-a-script)
    - [Example: Creating a Python Command](#example-creating-a-python-command)
  - [📌 Step 2: Make the Script Executable](#-step-2-make-the-script-executable)
  - [📌 Step 3: Move the Script to a System Directory](#-step-3-move-the-script-to-a-system-directory)
  - [📌 Step 4: Verify Your Command (Optional)](#-step-4-verify-your-command-optional)
  - [📌 Step 5: Testing Your Command with Pipes](#-step-5-testing-your-command-with-pipes)
  - [🎯 Summary](#-summary)
      - [🎯 Bonus: Examples in folder /commands](#-bonus-examples-in-folder-commands)
- [Creating Your own Shell](#creating-your-own-shell)
  - [📌Step 1: Create a Simple Shell in Python](#step-1-create-a-simple-shell-in-python)
  - [📌Step 2: Make the Shell Executable](#step-2-make-the-shell-executable)
    - [Pay Attention!](#pay-attention)
  - [📌Step 3: Change Default Shell to Your Own](#step-3-change-default-shell-to-your-own)
    - [Step 3.1](#step-31)
    - [Step 3.1](#step-31-1)
    - [Step 3.3: Change Your Default Shell](#step-33-change-your-default-shell)
  - [📌Step 4: Apply Changes](#step-4-apply-changes)
  - [🎯Revert Back to Bash (If Needed)](#revert-back-to-bash-if-needed)

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

# Creating Your own Shell
## 📌Step 1: Create a Simple Shell in Python
First, create a file called myshell.py and add the following code:

myshell.py (Basic Version)

```python
import os
import sys
import subprocess

def read_input():
    """Reads input from the user."""
    return input("mysh> ")

def parse_input(input_line):
    """Splits input into tokens (arguments)."""
    return input_line.strip().split()

def execute_command(command):
    """Executes the command entered by the user."""
    if not command:
        return  # If the command is empty, do nothing

    if command[0] == "exit":
        sys.exit(0)

    if command[0] == "cd":
        try:
            os.chdir(command[1])
        except IndexError:
            print("cd: missing argument")
        except FileNotFoundError:
            print(f"cd: no such directory: {command[1]}")
        return

    try:
        subprocess.run(command)
    except FileNotFoundError:
        print(f"{command[0]}: command not found")

def main():
    """Main shell loop."""
    while True:
        try:
            user_input = read_input()
            command = parse_input(user_input)
            execute_command(command)
        except KeyboardInterrupt:
            print("\nExiting shell...")
            sys.exit(0)

if __name__ == "__main__":
    main()

```

## 📌Step 2: Make the Shell Executable
Now, make myshell.py executable:

```sh
chmod +x myshell.py
```
You can now run it:
```sh
./myshell.py
```
This will launch your custom shell, and you can execute basic commands like ls, pwd, echo, and cd.

### Pay Attention!
The file /etc/passwd contains user account details, including the default shell. Before modifying it, create a backup:
```sh
sudo cp /etc/passwd /etc/passwd.bak
```

## 📌Step 3: Change Default Shell to Your Own
Now, let's replace Bash with your custom shell.
### Step 3.1 
Move `ishell.py` to `/bin` directory
```sh
cp ishell.py /bin/ishell
```
### Step 3.1 
Add Your Shell to /etc/shells
The system only allows shells listed in /etc/shells. To add yours:
```sh
vi /etc/shells
```
At the end of the file, add:
```
/bin/ishell
/usr/bin/ishell
```
Save and exit.
### Step 3.3: Change Your Default Shell
Open /etc/passwd with a text editor:
```sh
vi /etc/passwd
```
Find the line for your user (example for user):
```vi
user:x:1000:1000::/home/user:/bin/bash
```
Change /bin/bash to your custom shell’s full path:
```vi
user:x:1000:1000::/home/user:/bin/ishell
```
Save and exit (:wq then Enter).

## 📌Step 4: Apply Changes
To apply the new shell without logging out, run:
```sh
exec /home/user/myshell.py
```
Now, every time you log in, your system will start with your shell instead of Bash.

## 🎯Revert Back to Bash (If Needed)
If something goes wrong and you can't log in, switch to a TTY session:
- Press CTRL + ALT + F3 (or F2, F4, etc.).
- Log in with your username and password.
- Restore the original /etc/passwd:
```sh
sudo cp /etc/passwd.bak /etc/passwd
```
- then restart
```sh
reboot
```
Your shell will be back to Bash (/bin/bash).