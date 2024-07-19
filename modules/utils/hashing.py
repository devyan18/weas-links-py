import bcrypt
import base64

def hash_str(str: str) -> str:
    salt = bcrypt.gensalt()
    hashed_str = bcrypt.hashpw(str.encode('utf-8'), salt)
    hashed_str_b64 = base64.b64encode(hashed_str).decode('utf-8')
    return hashed_str_b64

def compare_str(str: str, hashed_str: str) -> bool:
    return bcrypt.checkpw(str.encode('utf-8'), base64.b64decode(hashed_str.encode('utf-8')))