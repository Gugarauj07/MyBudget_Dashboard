from db import db
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin


class Investimentos(db.Model, SerializerMixin):
    __tablename__ = 'Investimento'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer)
    name = db.Column(db.String(50))
    data = db.Column(db.DateTime)
    rendimentoANO = db.Column(db.Integer)
    risco = db.Column(db.String(50))
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categoria.id'))

    
    def __init__(self, name, descricao, data, valor, categoria, rendimentoANO, risco):
        self.name = name
        self.valor = valor
        self.descricao = descricao
        self.data = data
        self.categoria = categoria
        self.rendimentoANO = rendimentoANO
        self.risco = risco
