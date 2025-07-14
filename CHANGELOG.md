# 📜 CHANGELOG - ComuniVeci Post Service

Historial de cambios relevantes en el servicio de publicaciones de ComuniVeci.

---

## [1.1.0] - 2025-07-13

### ✨ Nuevas funcionalidades

- ➕ Se agregó endpoint POST /api/posts/user/:
  - Permite consultar publicaciones asociadas a un correo (útil para perfil.html).

- 📈 Se agregó endpoint GET /api/posts/summary/:
  - Devuelve número de publicaciones aprobadas, pendientes y total.
  - Diseñado para ser consumido por admin-service.

- ⚙️ Ajuste de settings.py para permitir configuración dinámica vía .env.
- 🧪 Se corrigieron imports y limpieza de configuración DRF.

---

## [1.0.0] - 2025-06-10

### 🚀 Funcionalidades implementadas

- ✅ Creación de publicaciones:
  - POST /api/posts/
  - Guarda solicitudes de publicación con campos como título, descripción, ubicación y contacto.

- ✅ Edición parcial de publicaciones:
  - PATCH /api/posts/{id}/
  - Permite modificar campos específicos de un post ya creado.

- ✅ Aprobación de publicaciones:
  - PATCH /api/posts/{id}/approve/
  - Marca una publicación como aprobada para ser visible públicamente.

- ✅ Eliminación de publicaciones:
  - DELETE /api/posts/{id}/delete/
  - Elimina permanentemente una publicación del sistema.

- ✅ Consulta de publicaciones pendientes:
  - GET /api/posts/pending/
  - Devuelve todas las publicaciones que aún no han sido aprobadas.

- ✅ Consulta de publicaciones aprobadas:
  - GET /api/posts/approved/
  - Devuelve todas las publicaciones aprobadas, pensadas para consumo por parte del map-service o el frontend público.

- ✅ Serializadores independientes con DRF.
- ✅ Adaptadores desacoplados para persistencia (MongoDB y en memoria).
- ✅ Arquitectura hexagonal aplicada.
- ✅ Documentación OpenAPI con drf-spectacular:
  - Swagger UI (/api/docs/swagger/)
  - Redoc (/api/docs/redoc/)
  - Esquema JSON (/api/schema/)
- ✅ Configuración por entorno vía archivo .env.

---

## 📅 Próximas versiones

- [ ] Autenticación y autorización.
- [ ] Paginación y filtros para consultas GET.
- [ ] Pruebas automáticas de casos de uso.
- [ ] Logging estructurado y manejo de errores detallado.
