# Golang-Scaffolding

Este proyecto es un generador de plantillas para aplicaciones Go. Utiliza un script en Python para crear automáticamente la estructura del proyecto y los archivos de código necesarios.

## Estructura del Proyecto

La estructura del proyecto que incluye este script es la siguiente:

```
Golang-scaffolding/
├── golang_codes/
│   ├── main.txt
│   ├── config.txt
│   ├── router.txt
│   ├── urlmapping.txt
└── script.py
```

## Requisitos

- **Python 3.x**: Asegúrate de tener Python instalado en tu sistema.
- **Go**: Debes tener Go instalado para compilar y ejecutar la aplicación generada.

## Instalación

1. Clona este repositorio o descarga los archivos a tu máquina local.
   
   ```bash
   git clone https://github.com/tu_usuario/Golang-scaffolding.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd Golang-scaffolding
   ```

3. Asegúrate de que los archivos de código Go necesarios estén en la carpeta `golang_codes`.

## Uso

### Ejecutar el Script

Para generar la estructura del proyecto, ejecuta el script `script.py`. Este script te pedirá un nombre de proyecto y generará la estructura de directorios y archivos necesarios.

#### En Mac y Linux

```bash
python3 script.py
```

#### En Windows

```bash
python script.py
```

### Ingreso del Nombre del Proyecto

Cuando se te pida, ingresa el nombre de tu proyecto utilizando solo guiones bajos (`_`). Por ejemplo, si deseas llamar a tu proyecto "NuevoProyecto" ingresa `nuevo_proyecto`.

### Resultado

El script generará la siguiente estructura dentro de un nuevo directorio con el nombre de tu proyecto:

```
nuevo_proyecto/
├── cmd/
│   ├── api/
│   │   └── main.go
│   └── config/
│       └── config.go
├── internal/
│   ├── router/
│   │   ├── router.go
│   │   └── urlmapping.go
│   ├── data/
│   ├── handlers/
│   ├── mock/
│   ├── models/
│   ├── services/
│   └── utils/
└── pkg/
```

### Sientete libre de modificarlo y adaptarlo a tus necesidades. Es el fin de estos pequeños proyectos.
