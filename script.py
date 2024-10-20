import os
from pathlib import Path

import os
from pathlib import Path

def initialize_project():
    project_name = str(input("Project name (use only names with '_' or '-'): "))
    
    while not (isinstance(project_name, str) and ('_' in project_name or '-' in project_name)):
        print("Invalid project name. Please try again.")
        project_name = str(input("Project name (use only names with '_' or '-'): "))

    stripped_name = ''.join(word.capitalize() for word in project_name.replace('-', '_').split('_'))

    project_path = Path("../" + stripped_name)

    project_path.mkdir(parents=True, exist_ok=True)

    os.chdir(project_path)

    return project_path, stripped_name


def create_file_in_dir(file_name, file_content, file_destination=None):
    if file_destination is None:
        file_path = Path(file_name)
    else:
        destination = Path(file_destination)
        destination.mkdir(parents=True, exist_ok=True)
        file_path = Path(destination / file_name)
    
    with file_path.open("w") as write_file:
        write_file.write(file_content)

    if file_name == "go.mod":
        os.system("go mod tidy")

def create_dirs(directories_str, destination=None):
    directories = directories_str.split(',')

    if destination == "internal":
        internal_path = Path("internal")
        for dir in directories:
            new_dir = Path(internal_path / dir.strip()) 
            new_dir.mkdir(parents=True, exist_ok=True)
            create_file_in_dir(str(dir + ".go"), f"package {dir}", new_dir)
    elif destination is None:
        for dir in directories:
            new_dir = Path(dir.strip()) 
            new_dir.mkdir(parents=True, exist_ok=True)
            create_file_in_dir(str(dir + ".go"), f"package {dir}", new_dir)

def edit_files(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_code_from_file(file_path):
    absolute_path = Path(__file__).parent / file_path 
    with open(absolute_path, "r") as file:
        return str(file.read())

project_path, project_name = initialize_project()


main_code =f"""
package main

import (
    "{project_name.lower()}/internal/router"
    "{project_name.lower()}/cmd/config"
)

func main() {{
    r := router.SetupRouter()
    r.Run(config.Port)
}}
"""

config_code = read_code_from_file("golang_codes/config.txt")
router_code = read_code_from_file("golang_codes/router.txt")
urlmapping_code = read_code_from_file("golang_codes/urlmapping.txt")

create_file_in_dir("main.go", main_code, "cmd/api")
create_file_in_dir("config.go", config_code, "cmd/config")
create_dirs("data,handlers,mock,models,router,services,utils", "internal")

edit_files("internal/router/router.go", router_code)
create_file_in_dir("urlmapping.go", urlmapping_code, "internal/router")

create_dirs("pkg")
create_file_in_dir("go.mod", f"module {project_name.lower()}")
