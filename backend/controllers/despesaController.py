from flask import Blueprint, request, jsonify
import sys
sys.path.append(r'C:\Work\myBudgetDashboard\backend')
from models import Despesas
from db import db

despesa_controller_bp = Blueprint('despesa_controller', __name__, url_prefix='/despesa')

@despesa_controller_bp.route('/', methods=['GET'])
def get_despesas():
    despesas = Despesas.query.all()
    return jsonify(despesas), 200

@despesa_controller_bp.route('/', methods=['POST'])
def create_despesa():
    data = request.get_json()
    data['name'] = Despesas(name=data['name'], valor=data['valor'], categoria=data['categoria'])
    db.session.add(data['name'])
    db.session.commit()
    return jsonify(data['name'].serialize()), 201

@despesa_controller_bp.route('/<int:despesa_id>', methods=['GET'])
def get_despesa(despesa_id):
    despesa = Despesas.query.get(despesa_id)
    if despesa:
        return jsonify(despesa.serialize()), 200
    else:
        return jsonify({'error': 'Despesas not found'}), 404


@despesa_controller_bp.route('/<int:despesa_id>', methods=['DELETE'])
def delete_despesa(despesa_id):
    despesa = Despesas.query.get(despesa_id)
    if not despesa:
        return jsonify({'error': 'Despesas not found'}), 404

    db.session.delete(despesa)
    db.session.commit()
    return '', 204