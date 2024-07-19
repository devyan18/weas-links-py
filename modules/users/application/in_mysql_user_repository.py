from modules.users.domain.user_entity import User
from modules.users.domain.user_repository import UserRepository
from db.connect_to_mysql import conn
from modules.utils.hashing import hash_str

class InMySqlUserRepository(UserRepository):
    def __init__(self):
        self.db = conn.cursor()

    def get_all(self) -> list[User]:
        try:
            self.db.execute("SELECT * FROM users")
            users = self.db.fetchall()
        except Exception as e:
            print(e)
            return []
        return [User(name=user[1], email=user[2], password=user[3], id=user[0]) for user in users]

    def get_by(self, id: str) -> User | None:
        user = None

        try:
            self.db.execute("SELECT * FROM users WHERE id = %s", (id,))
            user = self.db.fetchone()
        except Exception as e:
            print(e)
            return None

        if user:
            return User(name=user[1], email=user[2], password=user[3], id=user[0])
        return None

    def create(self, user: User) -> User:
        user.password = hash_str(user.password)
        
        try:
            self.db.execute("INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s)", (user.id, user.name, user.email, user.password))
            conn.commit()
        except Exception as e:
            print(e)
            return None
        
        created_user = self.get_by(user.id)
        return created_user
    
    def update_by(self, id: str, email: str, name: str) -> bool:
        
        try:
            self.db.execute("UPDATE users SET email = %s, name = %s WHERE id = %s", (email, name, id))
            conn.commit()
        except Exception as e:
            print(e)
            return False

        return True

    def delete_by(self, id: str) -> bool:
        
        try:
            self.db.execute("DELETE FROM users WHERE id = %s", (id,))
            conn.commit()
        except Exception as e:
            print(e)
            return False

        return True


