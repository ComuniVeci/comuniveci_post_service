import os
from dotenv import load_dotenv
from posts.infrastructure.persistence.mongo_repository import PostRepository
from posts.infrastructure.persistence.in_memory_repository import InMemoryPostRepository
from posts.infrastructure.persistence.db import get_db

load_dotenv()

_repo_instance = None

def get_post_repository():
    global _repo_instance
    mode = os.getenv("REPO_MODE", "mongo")
    if mode == "memory":
        # Usamos Singleton para mantener una sola instancia
        if _repo_instance is None:
            _repo_instance = InMemoryPostRepository()
        return _repo_instance
    else:
        db = get_db()
        return PostRepository(db)
