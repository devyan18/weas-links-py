from flask import Flask
from flask_cors import CORS

from modules.users.infrastructure.user_routes import UserRoutes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(UserRoutes)

    return app