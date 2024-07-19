from modules.utils.uid import generate_uid

class User ():
    def __init__(self, name: str, email: str, password: str, id: str = generate_uid()):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    
# if using ODM

