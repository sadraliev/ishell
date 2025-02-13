def execute_command(command):
    """Executes a command, supporting pipes and background execution."""
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

    # Handle pipes
    if "|" in command:
        commands = [cmd.strip().split() for cmd in " ".join(command).split("|")]
        processes = []
        prev_pipe = None

        for cmd in commands:
            if prev_pipe is None:
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            else:
                proc = subprocess.Popen(cmd, stdin=prev_pipe, stdout=subprocess.PIPE)
            prev_pipe = proc.stdout
            processes.append(proc)

        for proc in processes:
            proc.wait()
        return

    try:
        if background:
            subprocess.Popen(command)
        else:
            subprocess.run(command)
    except FileNotFoundError:
        print(f"{command[0]}: command not found")
