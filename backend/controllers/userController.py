from flask import Blueprint, request, jsonify
import sys
sys.path.append(r'C:\Work\myBudgetDashboard\backend')
from models import User
from db import db

user_controller_bp = Blueprint('user_controller', __name__, url_prefix='/users')

@user_controller_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [user.serialize() for user in users]}), 200

@user_controller_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201


@user_controller_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.serialize()), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@user_controller_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify(user.serialize()), 200


@user_controller_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return '', 204