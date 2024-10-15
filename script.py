import os
from pathlib import Path

def initialize_project():
    project_name = str(input("Project name (use only names with '_'): "))
    
    while not (isinstance(project_name, str) and "_" in project_name):
        print("Invalid project name. Please try again.")
        project_name = str(input("Project name (use only names with '_'): "))
    
    stripped_name = ''.join(word.capitalize() for word in project_name.split('_'))

    project_path = Path("../" + stripped_name)

    project_path.mkdir(parents=True, exist_ok=True)

    os.chdir(project_path)

    return project_path,stripped_name

def create_file_in_dir(file_name,file_content,file_destination=None):
    
    if file_destination == None:
        file_path=Path(file_name)
    
        with file_path.open("w") as write_file:
            write_file.write(file_content)

        if file_name == "go.mod":
            os.system("go mod tidy")
    else:
    
        directories = Path(file_destination)
        directories.mkdir(parents=True, exist_ok=True)

        file_path=Path(directories/file_name)
    
        with file_path.open("w") as write_file:
            write_file.write(file_content)

def create_dirs(directories_str,destination=None):
    directories = directories_str.split(',')

    if destination =="internal":
        internal_path=Path("internal")
        for dir in directories:

            new_dir = Path(internal_path/dir.strip()) 
            new_dir.mkdir(parents=True, exist_ok=True)

            create_file_in_dir(str(dir+".go"),f"package {dir}",new_dir)
    elif destination ==None:
        for dir in directories:

            new_dir = Path(dir.strip()) 
            new_dir.mkdir(parents=True, exist_ok=True)

            create_file_in_dir(str(dir+".go"),f"package {dir}",new_dir)



project_path,project_name=initialize_project()

create_file_in_dir("main.go","package main","cmd/api")

create_file_in_dir("config.go","package config","cmd/config")

create_dirs("data,handlers,mock,models,router,services,utils","internal")

create_dirs("pkg")

create_file_in_dir("go.mod",f"module {project_name.lower()}")
