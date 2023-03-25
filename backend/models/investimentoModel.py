from db import db
from sqlalchemy.sql import func


class Investimentos(db.Model):
    __tablename__ = 'Investimentos'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer)
    name = db.Column(db.String(50))
    data = db.Column(db.DateTime)
    rendimentoANO = db.Column(db.Integer)
    risco = db.Column(db.String(50))
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categorias.id'))

    
    def __init__(self, name, descricao, data, valor, categoria, rendimentoANO, risco):
        self.name = name
        self.valor = valor
        self.descricao = descricao
        self.data = data
        self.categoria = categoria
        self.rendimentoANO = rendimentoANO
        self.risco = risco


    def serialize(self):
        return {
            'name': self.name,
            'descricao': self.descricao,
            'rendimentoANO': self.rendimentoANO,
            'valor': self.valor
        }