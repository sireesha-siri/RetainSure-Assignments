from flask import Blueprint, request, jsonify

from models.user_model import (
    get_all_users, get_user_by_id, create_user, update_user,
    delete_user, search_users_by_name, login_user
)

user_routes = Blueprint('user_routes', __name__)

#----------------------------- HOME PAGE -----------------------------

@user_routes.route('/')
def home():
    return "User Management System"

#----------------------------- GET ALL USERS -----------------------------
@user_routes.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    result = [
        {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "password": user[3]
        }
        for user in users
    ]
    return jsonify(result)

#----------------------------- GET USER BY ID -----------------------------  

@user_routes.route('/user/<user_id>', methods=['GET'])
def get_user_route(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify({
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "password": user[3]
        })
    return jsonify({"error": "User not found"}), 404

#----------------------------- ADD A NEW USER -----------------------------

@user_routes.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    if not all(k in data for k in ['name', 'email', 'password']):
        return jsonify({"error": "Missing fields"}), 400
    create_user(data['name'], data['email'], data['password'])
    return jsonify({"message": "User created"}), 201

#----------------------------- UPDATE THE USER CREDENTIALS BY ID -----------------------------

@user_routes.route('/user/<user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    if not all(k in data for k in ['name', 'email']):
        return jsonify({"error": "Missing fields"}), 400
    update_user(user_id, data['name'], data['email'])
    return jsonify({"message": "User updated"}), 200

#----------------------------- DELETE THE USER -----------------------------

@user_routes.route('/user/<user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    delete_user(user_id)
    return jsonify({"message": f"User {user_id} deleted"}), 200

#----------------------------- SEARCH THE USER BY NAME -----------------------------

@user_routes.route('/search', methods=['GET'])
def search_users_route():
    name = request.args.get('name')
    if not name or not name.isalpha():
        return jsonify({"error": "Please provide a valid name"}), 400
    users = search_users_by_name(name)
    result = [{"id": u[0], "name": u[1], "email": u[2]} for u in users]
    return jsonify(result), 200

#----------------------------- LOGIN INTO THE ACCOUNT USING CREDENTIALS -----------------------------

@user_routes.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"status": "failed", "message": "Missing fields"}), 400

    user = login_user(email, password)
    if user:
        return jsonify({"status": "success", "user_id": user[0]}), 200
    return jsonify({"status": "failed", "message": "Invalid credentials"}), 401
