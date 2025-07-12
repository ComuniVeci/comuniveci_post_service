from abc import ABC, abstractmethod

class PostRepositoryInterface(ABC):
    @abstractmethod
    def create(self, post_data: dict) -> dict:
        pass

    @abstractmethod
    def update(self, post_data: dict) -> dict:
        pass

    @abstractmethod
    def find_by_id(self, post_id: str) -> dict:
        """Devuelve un post por su ID o None si no existe"""
        pass

    @abstractmethod
    def delete(self, post_id: str) -> None:
        pass

    @abstractmethod
    def find_pending(self) -> list[dict]:
        """Retorna todos los posts que no han sido aprobados aún."""
        pass

    @abstractmethod
    def find_approved(self) -> list[dict]:
        """Retorna todos los posts aprobados."""
        pass

    @abstractmethod
    def find_by_user_id(self, user_id) -> list[dict]:
        """Retorna todos los posts aprobados de un usuario."""
        pass