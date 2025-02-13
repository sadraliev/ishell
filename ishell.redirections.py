def execute_command(command):
    """Executes commands, supporting pipes, redirections, and background execution."""
    if not command:
        return

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

    background = False
    if command[-1] == "&":
        background = True
        command = command[:-1]

    # Handle redirections
    if ">" in command or "<" in command:
        if ">" in command:
            pos = command.index(">")
            filename = command[pos + 1]
            command = command[:pos]
            with open(filename, "w") as f:
                subprocess.run(command, stdout=f)
            return
        if "<" in command:
            pos = command.index("<")
            filename = command[pos + 1]
            command = command[:pos]
            with open(filename, "r") as f:
                subprocess.run(command, stdin=f)
            return

    try:
        if background:
            subprocess.Popen(command)
        else:
            subprocess.run(command)
    except FileNotFoundError:
        print(f"{command[0]}: command not found")
