from datetime import datetime
from posts.domain.repositories import PostRepositoryInterface

def create_post(data: dict, repository: PostRepositoryInterface) -> dict:
    """
    Crea un nuevo post utilizando el repositorio inyectado.
    """
    post_data = {
        "title": data["title"],
        "description": data.get("description", ""),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "address": data.get("address", ""),
        "contact_email": data.get("contact_email"),
        "images": data.get("images", []),
        "is_approved": False,
        "created_at": datetime.utcnow()
    }
    return repository.create(post_data)

