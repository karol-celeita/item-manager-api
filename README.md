# item-manager-api
Se implementan dos endpoints para "items": uno para crear un item y otro para listar los items. En routers, se define el endpoint y se llama a una función del servicio, usando esquemas para el body y la respuesta. El servicio actúa como capa intermedia y llama al repositorio.

* Se usara sqlite pero el sistema está preparado para soportar PostgreSQL solo ingrese la libreria de psycopg2

## Ejecutar app:

``` bash
# Clonar
$ git clone https://github.com/karol-celeita/api-item-manager.git
# Ingresar al app
$ cd app
# Construir entorno
$ python -m venv venv
# Activar entorno
$ source venv/Scripts/activate
# Ejecutar app
$ python main.py
```

📝 Pruebas
Para ejecutar las pruebas, utiliza:
``` bash
pytest --cov=app
```
Docker
Para construir y ejecutar el contenedor Docker:
``` bash
docker-compose -f Docker/docker-compose.yml up -d
```

## Flujos de Trabajo 

Utilizamos Gitflow para gestionar las ramas:
![flujo de trabajo](/assets/flujo-git.png)

## Estructura del proyecto

```
├── app
│ ├── models
│ │ ├── __init__.py
│ │ └── items.py
│ ├── repositories
│ │ ├── __init__.py
│ │ └── item_repository.py
│ ├── routers
│ │ ├── __init__.py
│ │ └── items.py
│ ├── schemas
│ │ ├── __init__.py
│ │ └── items_schemas.py
│ ├── services
│ │ ├── __init__.py
│ │ └── items_service.py
│ ├── __init__.py
│ ├── constants.py
│ ├── database.py
│ └── main.py
├── Docker
│ ├── .dockerignore
│ ├── docker-compose.yml
│ └── Dockerfile
├── assets
│ └── flujo-git.png
├── tests
│ ├── __init__.py
│ └── test_routers_items.py
├── requirements.txt
├── .env_example
├── .gitignore
└── readme.md
```