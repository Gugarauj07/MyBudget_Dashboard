from flask import Blueprint, request, jsonify
import sys
sys.path.append(r'C:\Work\myBudgetDashboard\backend')
from models import Receitas
from db import db

receita_controller_bp = Blueprint('receita_controller', __name__, url_prefix='/receita')

@receita_controller_bp.route('/', methods=['GET'])
def get_receitas():
    receitas = Receitas.query.all()
    return jsonify({'receitas': [receita.serialize() for receita in receitas]}), 200

@receita_controller_bp.route('/', methods=['POST'])
def create_receitas():
    data = request.get_json()
    receita = Receitas(name=data['name'], descricao=data['descricao'], valor=data['valor'], categoria=data['categoria'])
    db.session.add(receita)
    db.session.commit()
    return jsonify(receita.serialize()), 201

@receita_controller_bp.route('/<int:receitas_id>', methods=['GET'])
def get_receitas(receitas_id):
    receita = Receitas.query.get(receitas_id)
    if receita:
        return jsonify(receita.serialize()), 200
    else:
        return jsonify({'error': 'Receitas not found'}), 404


@receita_controller_bp.route('/<int:receitas_id>', methods=['DELETE'])
def delete_receitas(receitas_id):
    receita = Receitas.query.get(receitas_id)
    if not receita:
        return jsonify({'error': 'Receitas not found'}), 404

    db.session.delete(receita)
    db.session.commit()
    return '', 204