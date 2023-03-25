from flask import Blueprint, request, jsonify
import sys
sys.path.append(r'C:\Work\myBudgetDashboard\backend')
from models import Categorias
from db import db

categoria_controller_bp = Blueprint('categoria_controller', __name__, url_prefix='/categoria')

@categoria_controller_bp.route('/', methods=['GET'])
def get_categorias():
    categorias = Categorias.query.all()
    return jsonify({'categoria': [categoria.serialize() for categoria in categorias]}), 200

@categoria_controller_bp.route('/', methods=['POST'])
def create_categoria():
    data = request.get_json()
    categoria = Categorias(name=data['name'], descricao=data['descricao'], tipo=data['tipo'])
    db.session.add(categoria)
    db.session.commit()
    return jsonify(categoria.serialize()), 201

@categoria_controller_bp.route('/<int:categoria_id>', methods=['GET'])
def get_categoria(categoria_id):
    categoria = Categorias.query.get(categoria_id)
    if categoria:
        return jsonify(categoria.serialize()), 200
    else:
        return jsonify({'error': 'Categorias not found'}), 404


@categoria_controller_bp.route('/<int:categoria_id>', methods=['DELETE'])
def delete_categoria(categoria_id):
    categoria = Categorias.query.get(categoria_id)
    if not categoria:
        return jsonify({'error': 'Categorias not found'}), 404

    db.session.delete(categoria)
    db.session.commit()
    return '', 204