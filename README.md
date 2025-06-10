# ComuniVeci – Post Service

Este servicio es responsable de la creación, edición, aprobación, eliminación y consulta de publicaciones dentro del sistema distribuido ComuniVeci. Fue desarrollado siguiendo principios de arquitectura hexagonal y expone una API RESTful desacoplada que puede ser consumida por el frontend u otros servicios como map-service.

## ⚙️ Tecnologías utilizadas

- Python 3.13
- Django 5.2
- Django REST Framework
- Poetry + pyenv para gestión del entorno
- MongoDB (opcional) o repositorio en memoria
- drf-spectacular (documentación Swagger / OpenAPI)

## 🚀 Instalación y configuración

1. Clonar el repositorio

```bash
git clone https://github.com/ComuniVeci/comuniveci_post_service
cd comuniveci-post-service
```

2. Instalar dependencias

```bash
poetry install
```

3. Crear el archivo de entorno

```bash
cp .env.example .env
```

Modificar el archivo .env según tu entorno local:
```bash
REPO_MODE=memory  # Opciones: memory o mongo
MONGO_URI=mongodb://localhost:27017/
DB_NAME=communiveci
```

4. Ejecutar el servidor de desarrollo

```bash
poetry run python manage.py runserver
```

## 🧪 API REST

Documentación disponible en:

- Swagger UI: http://127.0.0.1:8000/api/docs/swagger/
- Redoc: http://127.0.0.1:8000/api/docs/redoc/
- Esquema OpenAPI (JSON): http://127.0.0.1:8000/api/schema/

## 🧭 Endpoints disponibles

| Método  | Endpoint                          | Descripción                                 |
|---------|-----------------------------------|---------------------------------------------|
| POST    | /api/posts/                       | Crea una nueva solicitud de publicación     |
| PATCH   | /api/posts/{id}/                  | Edita parcialmente una publicación          |
| PATCH   | /api/posts/{id}/approve/          | Aprueba una publicación                     |
| DELETE  | /api/posts/{id}/delete/           | Elimina una publicación                     |
| GET     | /api/posts/pending/               | Obtiene todas las publicaciones pendientes  |
| GET     | /api/posts/approved/              | Obtiene todas las publicaciones aprobadas   |

## 📁 Estructura del proyecto (Hexagonal)

- domain/: entidades, interfaces y puertos
- usecases/: lógica de aplicación desacoplada
- infrastructure/:
  - api/: vistas (adaptadores primarios)
  - serializers/: serializadores DRF
  - persistence/: adaptadores secundarios (repositorios)
- settings/, manage.py: configuración Django

## 💡 Modo sin base de datos

Si usas REPO_MODE=memory, todos los datos viven solo durante la ejecución. Ideal para pruebas sin MongoDB.

## 🔒 Seguridad

Este servicio no incluye autenticación ni autorización.

## 📦 Comandos útiles

Crear post de prueba:

```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Fuga de agua",
    "description": "Hay una fuga en la calle 12",
    "latitude": 4.65,
    "longitude": -74.08,
    "address": "Calle 12 #3-45",
    "contact_email": "vecino@ejemplo.com",
    "images": []
  }' | jq
```

Listar publicaciones pendientes:

```bash
curl -s http://127.0.0.1:8000/api/posts/pending/ | jq
```

Aprobar publicación:

```bash
curl -X PATCH http://127.0.0.1:8000/api/posts/<post_id>/approve/
```

Eliminar publicación:

```bash
curl -X DELETE http://127.0.0.1:8000/api/posts/<post_id>/delete/
```

Listar publicaciones aprobadas:

```bash
curl -s http://127.0.0.1:8000/api/posts/approved/ | jq