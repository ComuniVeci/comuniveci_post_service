from posts.domain.repositories import PostRepositoryInterface
from uuid import uuid4
from datetime import datetime

class InMemoryPostRepository(PostRepositoryInterface):
    def __init__(self):
        self._data = {}  # Simula la base de datos como un diccionario
    
    def create(self, post_data):
        post_id = str(uuid4())
        post_data["_id"] = post_id
        post_data["created_at"] = datetime.utcnow()
        self._data[post_id] = post_data
        return post_data

    def update(self, post_data):
        post_id = post_data["_id"]
        self._data[post_id] = post_data  # Sobrescribe sin cambiar el id
        return post_data

    def find_by_id(self, post_id):
        return self._data.get(post_id)
    
    def delete(self, post_id):
        if post_id in self._data:
            del self._data[post_id]

    def find_pending(self):
        return [post for post in self._data.values() if not post.get("is_approved", False)]
    
    def find_approved(self):
        return [post for post in self._data.values() if post.get("is_approved") is True]

