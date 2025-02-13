#!/usr/bin/env python3

import os
import sys
import subprocess
import getpass
import socket
import random

def read_input():
    """A dynamic, fun, and stylish shell prompt with random user titles and quotes."""
    
    # Get system details
    user = getpass.getuser()
    host = socket.gethostname()
    cwd = os.getcwd()

    # Define colors
    GREEN = "\033[1;32m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    PURPLE = "\033[1;35m"
    RESET = "\033[0m"

    # Random Titles for the User
    titles = [
        "The Fearless Coder 🏆",
        "The Shell Master 🐚",
        "The Cyber Ninja 🥷",
        "The Command Line Sorcerer 🔮",
        "The Terminal Hacker 👾",
        "The Bash Warrior ⚔️",
        "The Code Samurai 🏯",
        "The Root of All Power ⚡",
        "The CLI Overlord 👑",
        "The Digital Alchemist ⚗️",
        "The Quantum Dev 🪐",
        "The Matrix Architect 🖥️",
    ]

    # Random Quotes
    quotes = [
        "Keep coding, keep conquering. 💻🔥",
        "A bug is just an undocumented feature. 🐞✨",
        "One shell to rule them all. 👑🐚",
        "Eat, Sleep, Code, Repeat. 🔄",
        "Real hackers use the terminal. 👨‍💻⚡",
        "Don't fear the CLI. Master it. 😈",
        "sudo make me a sandwich? Nope. 🍔",
        "The quieter you become, the more you hear. 🎧",
        "May your uptime be long and your errors be few. 🚀",
        "CTRL+C is for the weak. 😈",
        "rm -rf /? Only in nightmares. 💀",
        "404: Fear Not Found. 🦸",
    ]

    # Pick a random title and phrase
    user_title = random.choice(titles)
    user_quote = random.choice(quotes)

    # Cool Emojis 🎭 🏆 ⚔️
    prompt = (
        f"{PURPLE}🎭 {user}@{host} {RESET}"
        f"{BLUE}📂 {cwd} {RESET}\n"
        f"{CYAN}💬 {user_title}: {user_quote} {RESET}\n"
        f"{GREEN}⚡ iShell>{RESET} "
    )

    return input(prompt)



def parse_input(input_line):
    """Splits input into tokens (arguments)."""
    return input_line.strip().split()

def execute_command(command):
    """Executes a command entered by the user."""
    if not command:
        return  # Ignore empty commands

    if command[0] == "exit":  # Exit the shell
        sys.exit(0)

    if command[0] == "cd":  # Change directory
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
