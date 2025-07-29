import sys
from utils.files.directory import print_project_tree, print_file_data_summary
from logs.log import create_log

def main():
    if len(sys.argv) < 2:
        print("Usage: python scan.py <project_path>")
        sys.exit(1)

    project_path = sys.argv[1]
    create_log('info', f'scanning directory {project_path}')
    
    print_project_tree(project_path)
    
    print_file_data_summary(project_path)

if __name__ == "__main__":
    main()
