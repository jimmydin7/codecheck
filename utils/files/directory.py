import os
from logs.log import create_log
from .filedata import FileData

def print_project_tree(base_path, prefix=""):
    try:
        entries = sorted(os.listdir(base_path))
    except FileNotFoundError:
        create_log('error', f"Directory '{base_path}' not found.")
        return
    except PermissionError:
        create_log('error', f"Permission denied by os -> '{base_path}'")
        return

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        path = os.path.join(base_path, entry)
        if os.path.isdir(path):
            extension = "    " if i == len(entries) - 1 else "│   "
            print_project_tree(path, prefix + extension)

def collect_files(base_path):
    file_objects = []
    for root, dirs, files in os.walk(base_path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            file_objects.append(FileData(full_path))
    return file_objects

def print_file_data_summary(base_path):
    files = collect_files(base_path)
    print("\nFile summary:")
    for f in files:
        print(f"{f.name} | Ext: {f.extension} | Path: {f.full_path} | Size: {f.size} bytes")
        print(f"Source code:")
        print(f.source_code)
        print("-" * 50)
