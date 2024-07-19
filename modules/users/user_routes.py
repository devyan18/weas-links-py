from flask import Blueprint, request, jsonify

from modules.users.user_entity import User
from modules.users.in_mysql_user_repository import InMySqlUserRepository

UserRoutes = Blueprint('users', __name__, url_prefix='/users')
repository = InMySqlUserRepository()

@UserRoutes.route('/', methods=['GET'])
def index():
    return jsonify([user.json() for user in repository.get_all()]), 200

@UserRoutes.route('/<id>', methods=['GET'])
def show(id):
    try:
        return jsonify(repository.get_by(id).json()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@UserRoutes.route('/', methods=['POST'])
def create():
    data = request.json

    user = User(data['name'], data['email'], data['password'])
    print(user.json())
    new_user = None

    try:
        new_user = repository.create(user)
    except Exception as e:
        return jsonify({'message': str(e)}), 400

    return jsonify(new_user.json()), 201

@UserRoutes.route('/<id>', methods=['PATCH'])
def update(id):
    data = request.json

    try:
        repository.update_by(id, data["email"], data['name'])
    except Exception as e:
        return jsonify({'message': str(e)}), 400

    return jsonify({'message': 'User updated'}), 200


@UserRoutes.route('/<id>', methods=['DELETE'])
def delete(id):
    try:
        repository.delete_by(id)
    except Exception as e:
        return jsonify({'message': str(e)}), 400

    return jsonify({'message': 'User deleted'}), 200