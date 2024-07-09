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
# Instalar dependencias
$ pip install -r requirements.txt
# Crear .env basadado en el .env_example
$ copy .env_example .env
# Ejecutar app
$ python main.py
```

## 📝 Pruebas
Utiliza el siguiente comando para ejecutar el coverage:
``` bash
pytest --cov=app
```
## Docker
Para levantar la aplicación con docker ejecutar:
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

## Explicación de la Arquitectura y Comunicación entre Capas
### Routers (app/routers/items.py):

Define los endpoints de la API utilizando FastAPI. Aquí se especifican los métodos HTTP (GET, POST, etc.) y se llama a funciones del servicio correspondiente para manejar las peticiones y respuestas.

### Services (app/services/items_service.py):

Esta capa actúa como una interfaz entre los routers y los repositorios. Contiene la lógica de negocio de la aplicación y puede realizar validaciones adicionales, autorizaciones, o cualquier otra lógica antes de llamar a los métodos de los repositorios para acceder a los datos.

### Repositories (app/repositories/item_repository/item_repo.py):

Aquí se implementa la lógica de acceso a datos, que generalmente involucra operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la base de datos o el almacenamiento persistente. Los repositorios reciben entidades de datos (generalmente utilizando los esquemas definidos en schemas) y las convierten en modelos de datos que son utilizados para interactuar con la capa de almacenamiento.
### Models (app/models/items.py) y Schemas (app/schemas/items_schemas.py):

Models: Definen la estructura de los datos en la base de datos, reflejando las tablas o colecciones que se utilizarán.
Schemas: Definen las estructuras de datos para las solicitudes HTTP (esquemas de entrada) y las respuestas (esquemas de salida). Estos esquemas son útiles para la validación de datos y la serialización/deserialización de objetos Python a/desde JSON.
## Comunicación y Flujo de Datos
* Routers utilizan los esquemas definidos en schemas para validar las solicitudes de entrada y estructurar las respuestas.
* Services manejan la lógica de negocio y orquestan la interacción entre los routers y los repositorios.
* Repositories interactúan directamente con la capa de almacenamiento, utilizando los modelos de datos definidos en models.