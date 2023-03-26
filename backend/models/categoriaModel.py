from db import db
from sqlalchemy_serializer import SerializerMixin

class Categorias(db.Model, SerializerMixin):
    __tablename__ = 'Categoria'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    descricao = db.Column(db.String(250))
    limite = db.Column(db.Integer)
    prioridade = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    # despesas = db.relationship('Despesa', backref='Categoria')
    # receitas = db.relationship('Receita', backref='Categoria')
    # investimentos = db.relationship('Investimento', backref='Categoria')

    def __init__(self, name, descricao,tipo, limite=None, prioridade=None):
        self.name = name
        self.descricao = descricao
        self.limite = limite
        self.prioridade = prioridade
        self.tipo = tipo