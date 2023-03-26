from flask import Blueprint, request, jsonify
import sys
sys.path.append(r'C:\Work\myBudgetDashboard\backend')
from models import Metas
from db import db

meta_controller_bp = Blueprint('meta_controller', __name__, url_prefix='/meta')

@meta_controller_bp.route('/', methods=['GET'])
def get_metas():
    metas = Metas.query.all()
    return jsonify({'metas': [meta.serialize() for meta in metas]}), 200

@meta_controller_bp.route('/', methods=['POST'])
def create_metas():
    data = request.get_json()
    meta = Metas(name=data['name'], dataFinal=data['dataFinal'], valorEstimado=data['valorEstimado'])
    db.session.add(meta)
    db.session.commit()
    return jsonify(meta.serialize()), 201

@meta_controller_bp.route('/<int:metas_id>', methods=['GET'])
def get_meta(metas_id):
    meta = Metas.query.get(metas_id)
    if meta:
        return jsonify(meta.serialize()), 200
    else:
        return jsonify({'error': 'Metas not found'}), 404


@meta_controller_bp.route('/<int:metas_id>', methods=['DELETE'])
def delete_meta(metas_id):
    meta = Metas.query.get(metas_id)
    if not meta:
        return jsonify({'error': 'Metas not found'}), 404

    db.session.delete(meta)
    db.session.commit()
    return '', 204