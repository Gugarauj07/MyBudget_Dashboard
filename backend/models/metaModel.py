from db import db
from sqlalchemy.sql import func


class Metas(db.Model):
    __tablename__ = 'Metas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    dataInicial = db.Column(db.DateTime)
    dataFinal = db.Column(db.DateTime)
    valorEstimado = db.Column(db.Integer)
    
    def __init__(self, name, descricao, dataInicial, dataFinal, valorEstimado):
        self.name = name
        self.valorEstimado = valorEstimado
        self.descricao = descricao
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal

    def serialize(self):
        return {
            'name': self.name,
            'descricao': self.descricao,
            'dataFinal': self.dataFinal,
            'valorEstimado': self.valorEstimado
        }