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

