from db import db

class Categorias(db.Model):
    __tablename__ = 'Categorias'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    descricao = db.Column(db.String(250))
    limite = db.Column(db.Integer)
    prioridade = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    despesas = db.relationship('Despesas', backref='Categorias')
    receitas = db.relationship('Receitas', backref='Receitas')
    investimentos = db.relationship('Investimentos', backref='Receitas')

    def __init__(self, name, descricao,tipo, limite=None, prioridade=None):
        self.name = name
        self.descricao = descricao
        self.limite = limite
        self.prioridade = prioridade
        self.tipo = tipo
    
    def serialize(self):
        return {
            'name': self.name,
            'descricao': self.descricao,
            'limite': self.limite,
            'prioridade': self.prioridade,
            'tipo': self.tipo
        }