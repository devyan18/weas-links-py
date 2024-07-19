from abc import ABC, abstractmethod
from modules.users.user_entity import User

class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def get_by(self, id: str) -> User | None:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def update_by(self, id: str, email: str, name: str) -> bool:
        pass

    @abstractmethod
    def delete_by(self, id: str) -> bool:
        pass


