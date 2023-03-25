from db import db
from sqlalchemy.sql import func


class Receitas(db.Model):
    __tablename__ = 'Receitas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    data = db.Column(db.DateTime, server_default=func.now())
    valor = db.Column(db.Integer)
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categorias.id'))


    def __init__(self, name, descricao, valor, categoria):
        self.name = name
        self.valor = valor
        self.descricao = descricao 
        self.categoria = categoria    

    
    def serialize(self):
        return {
            'name': self.name,
            'descricao': self.descricao,
            'valor': self.valor,
            'categoria': self.categoria
        }