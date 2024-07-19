from dotenv import load_dotenv
import os

load_dotenv()

ENV = {
    "PORT": os.getenv('PORT', 4000), 
    "DB_HOST": os.getenv('DB_HOST', 'localhost'),
    "DB_USER": os.getenv('DB_USER', 'root'),
    "DB_PASSWORD": os.getenv('DB_PASSWORD', 'root'),
    "DB_NAME": os.getenv('DB_NAME', 'test')
}