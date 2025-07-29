import os
from logs.log import create_log

def print_project_tree(base_path, prefix=""):
    try:
        entries = sorted(os.listdir(base_path))
    except FileNotFoundError:
        create_log('error', f"Directory '{base_path}' not found.")
    except PermissionError:
        create_log('error', f"Permission denied by os -> '{base_path}'")

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        path = os.path.join(base_path, entry)
        if os.path.isdir(path):
            extension = "    " if i == len(entries) - 1 else "│   "
            print_project_tree(path, prefix + extension)
