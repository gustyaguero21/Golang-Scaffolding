import os
from pathlib import Path

def initialize_project():
    project_name = str(input("Project name (use only names with '_'): "))
    
    while not (isinstance(project_name, str) and "_" in project_name):
        print("Invalid project name. Please try again.")
        project_name = str(input("Project name (use only names with '_'): "))
    
    project_name = ''.join(word.capitalize() for word in project_name.split('_'))

    # Define la ruta del proyecto
    project_path = Path("../" + project_name)

    # Crea la carpeta del proyecto si no existe
    project_path.mkdir(parents=True, exist_ok=True)

    # Cambia el directorio de trabajo actual al nuevo directorio del proyecto
    os.chdir(project_path)

    return project_path, project_name

def create_file(project_name, file_name, file_content):
    
    file_path = Path(file_name)

    with file_path.open("w") as write_file:
        write_file.write(file_content + " " + project_name.lower())

    if file_name =="go.mod":
        os.system("go mod tidy")

def create_dir(dir_name):
    # Crea el directorio en el directorio de trabajo actual
    directories = Path(dir_name)
    directories.mkdir(parents=True, exist_ok=True)

# Inicializar el proyecto
project_path, project_name = initialize_project()

# Crear un archivo
create_file(project_name, "go.mod", "module")

# Crear un directorio
create_dir("cmd/api")
