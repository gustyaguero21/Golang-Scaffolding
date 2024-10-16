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

def edit_files(file_path, content):
    # Escribe o sobrescribe el contenido en el archivo dado
    with open(file_path, 'w') as file:
        file.write(content)
    


project_path,project_name=initialize_project()

main_code="""
package main

import (
	"newapp/cmd/config"
	"newapp/internal/router"
)

func main() {

	router := router.SetupRouter()

	router.Run(config.Port)
}
"""

create_file_in_dir("main.go",main_code,"cmd/api")

config_code="""
package config

//router params

const (
	Port = ":8080"
)

"""

create_file_in_dir("config.go",config_code,"cmd/config")

create_dirs("data,handlers,mock,models,router,services,utils","internal")

router_code = """
package router

import "github.com/gin-gonic/gin"

func SetupRouter() *gin.Engine {
    router := gin.Default()

    Urlmapping(router)

    return router
}
"""

urlmapping_code= """
package router

import "github.com/gin-gonic/gin"

func Urlmapping(router *gin.Engine) {
    api := router.Group("/api/v1")
    api.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
}
"""


edit_files("internal/router/router.go", router_code)
create_file_in_dir("urlmapping.go",urlmapping_code,"internal/router")


create_dirs("pkg")

create_file_in_dir("go.mod",f"module {project_name.lower()}")


