from modules.users.domain.user_entity import User
from modules.users.domain.user_repository import UserRepository
from modules.utils.hashing import hash_str

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.__user_list: list[User] = []

    def __get_index_by__(self, id: str) -> int | None:
        for i, user in enumerate(self.__user_list):
            if user.id == id:
                return i
        return None

    def get_all(self) -> list[User]:
        return self.__user_list

    def get_by(self, id: str) -> User | None:

        if not id:
            raise Exception('Invalid id')
        
        index = self.__get_index_by__(id)

        if index is None:
            raise Exception('User not found')
        
        user_found = self.__user_list[index]

        return  user_found

    def create(self, user: User) -> User:
        if user.email in [u.email for u in self.__user_list]:
            raise Exception('User already exists')
        
        user.password = hash_str(user.password)

        self.__user_list.append(user)
        return user

    def update_by(self, id: str, email: str, name: str) -> bool:
        index = self.__get_index_by__(id)

        if index is None:
            raise Exception('User not found')

        self.__user_list[index].email = email
        self.__user_list[index].name = name

        return True

    def delete_by(self, id: str) -> bool:
        index = self.__get_index_by__(id)

        if index is None:
            raise Exception('User not found')

        self.__user_list.pop(index)

        return True


        
    