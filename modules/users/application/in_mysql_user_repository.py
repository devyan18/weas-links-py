from modules.users.domain.user_entity import User
from modules.users.domain.user_repository import UserRepository
from db.connect_to_mysql import conn
from modules.utils.hashing import hash_str

class InMySqlUserRepository(UserRepository):
    def __init__(self):
        self.db = conn.cursor()

    def get_all(self) -> list[User]:
        self.db.execute("SELECT * FROM users")
        users = self.db.fetchall()
        return [User(name=user[1], email=user[2], password=user[3], id=user[0]) for user in users]

    def get_by(self, id: str) -> User | None:
        self.db.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = self.db.fetchone()
        if user:
            return User(name=user[1], email=user[2], password=user[3], id=user[0])
        return None

    def create(self, user: User) -> User:
        user.password = hash_str(user.password)
        self.db.execute("INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s)", (user.id, user.name, user.email, user.password))
        conn.commit()
        
        created_user = self.get_by(user.id)
        return created_user
    
    def update_by(self, id: str, email: str, name: str) -> bool:
        self.db.execute("UPDATE users SET email = %s, name = %s WHERE id = %s", (email, name, id))
        conn.commit()
        return True

    def delete_by(self, id: str) -> bool:
        self.db.execute("DELETE FROM users WHERE id = %s", (id,))
        conn.commit()
        return True


