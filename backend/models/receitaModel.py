from db import db
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin


class Receitas(db.Model, SerializerMixin):
    __tablename__ = 'Receita'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    data = db.Column(db.DateTime, server_default=func.now())
    valor = db.Column(db.Integer)
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categoria.id'))


    def __init__(self, name, descricao, valor, categoria):
        self.name = name
        self.valor = valor
        self.descricao = descricao 
        self.categoria = categoria    

