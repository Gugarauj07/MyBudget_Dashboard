from db import db
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin


class Metas(db.Model, SerializerMixin):
    __tablename__ = 'Meta'

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