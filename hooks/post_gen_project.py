"""
This script runs after after your project has been generated. It scans through
all the files, looking for to-do items and collects them into a todo.txt file.
"""

import os
from pathlib import Path


ROOT_DIR = Path(os.getcwd())


def _parse(line):
    todo = line.find("TODO:")
    msg = line[todo + len("TODO:") :]
    return msg.strip()


def get_todo(file):
    with open(file, "r") as f:
        lines = f.readlines()

    todos = []
    for i, line in enumerate(lines):
        if "TODO" not in line:
            continue
        else:
            msg = _parse(line)
            todos.append(f"{file}:{i + 1} {msg}")
    return todos


all_files = []
for root, _, files in os.walk(ROOT_DIR):
    all_files.extend([Path(root) / file for file in files])

todos = []
for file in all_files:
    todos.extend(get_todo(file))

with open("todo.txt", "w") as f:
    f.write("\n".join(todos))
