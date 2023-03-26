from flask import Blueprint, request, jsonify
import sys
sys.path.append(r'C:\Work\myBudgetDashboard\backend')
from models import Investimentos
from db import db

investimento_controller_bp = Blueprint('investimento_controller', __name__, url_prefix='/investimento')

@investimento_controller_bp.route('/', methods=['GET'])
def get_investimentos():
    investimentos = Investimentos.query.all()
    return jsonify({'investimentos': [investimento.serialize() for investimento in investimentos]}), 200

@investimento_controller_bp.route('/', methods=['POST'])
def create_investimentos():
    data = request.get_json()
    investimento = Investimentos(name=data['name'], descricao=data['descricao'], valor=data['valor'], categoria=data['categoria'], risco=data['risco'], rendimentoANO=data['rendimentoANO'])
    db.session.add(investimento)
    db.session.commit()
    return jsonify(investimento.serialize()), 201

@investimento_controller_bp.route('/<int:investimentos_id>', methods=['GET'])
def get_investimentos(investimentos_id):
    investimento = Investimentos.query.get(investimentos_id)
    if investimento:
        return jsonify(investimento.serialize()), 200
    else:
        return jsonify({'error': 'Investimentos not found'}), 404


@investimento_controller_bp.route('/<int:investimentos_id>', methods=['DELETE'])
def delete_investimentos(investimentos_id):
    investimento = Investimentos.query.get(investimentos_id)
    if not investimento:
        return jsonify({'error': 'Investimentos not found'}), 404

    db.session.delete(investimento)
    db.session.commit()
    return '', 204