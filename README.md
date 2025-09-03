# API de Gestión de Tareas (API_Proyect)

Este proyecto es una API RESTful diseñada para la gestión de tareas. Permite a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre tareas, así como filtrarlas según diferentes criterios.

## ✨ Características

- **Gestión completa de tareas**: Crea, visualiza, edita y elimina tareas.
- **Listado de tareas**: Obtén una lista de todas las tareas existentes.
- **Filtrado avanzado**: Filtra tareas por su fecha límite y otros posibles estados.
- **Arquitectura REST**: Sigue los principios de diseño REST para una API limpia y predecible.

## 🚀 Puesta en Marcha

Sigue estos pasos para tener una copia local del proyecto funcionando.

### Prerrequisitos

Asegúrate de tener instalado Python 3.8+ y pip.

- Python 3.8+
- pip

### Instalación

1.  **Clona el repositorio**
    ```sh
    git clone https://github.com/Ferfelipe30/API_Proyect.git
    cd API_Proyect
    ```

2.  **Crea y activa un entorno virtual**
    ```sh
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias**
    (Asegúrate de tener un archivo `requirements.txt` con las librerías como Flask o FastAPI)
    ```sh
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación**
    (Este comando puede variar dependiendo del framework que uses)
    ```sh
    # Ejemplo para Flask
    flask run

    # Ejemplo para FastAPI con uvicorn
    uvicorn main:app --reload
    ```

## ⚙️ Uso de la API (Endpoints)

La API proporciona los siguientes endpoints para interactuar con los recursos de tareas.

| Método HTTP | Endpoint              | Descripción                                                               |
| :---------- | :-------------------- | :------------------------------------------------------------------------ |
| `GET`       | `/tasks`              | Obtiene una lista de todas las tareas. Acepta filtros como query params.  |
| `POST`      | `/tasks`              | Crea una nueva tarea.                                                     |
| `GET`       | `/tasks/{task_id}`    | Obtiene los detalles de una tarea específica por su ID.                   |
| `PUT`       | `/tasks/{task_id}`    | Actualiza una tarea existente por su ID.                                  |
| `DELETE`    | `/tasks/{task_id}`    | Elimina una tarea por su ID.                                              |

### Ejemplo de Filtrado

Para filtrar tareas por su fecha límite, puedes hacer una petición `GET` de la siguiente manera:

```
GET /tasks?due_date=2024-12-31
```

## 🤝 Contribuciones

Las contribuciones son lo que hace que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear. Cualquier contribución que hagas será **muy apreciada**.

1.  Haz un Fork del proyecto.
2.  Crea tu rama de características (`git checkout -b feature/AmazingFeature`).
3.  Confirma tus cambios (`git commit -m 'Add some AmazingFeature'`).
4.  Empuja a la rama (`git push origin feature/AmazingFeature`).
5.  Abre una Pull Request.

