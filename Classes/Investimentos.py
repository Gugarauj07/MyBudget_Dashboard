from connect.connectBD import conn, cursor

class Investimentos:
    def __init__(self, nome, valor, rendimento, risco, categoria, data, descricao):
        self.valor = valor
        self.rendimento = rendimento
        self.categoria = categoria
        self.risco = risco
        self.data = data
        self.nome = nome
        self.descricao = descricao
        
    def addInvestimentos(self):
        cursor.execute(f"SELECT id FROM categoria WHERE nome = '{self.categoria}'")
        categoria_id = cursor.fetchall()[0][0]
        cursor.execute(f'INSERT INTO investimentos (nome, data, categoria_id, risco, descricao, valor, rendimentoANO) VALUES("{self.nome}", "{self.data}", {categoria_id},{self.risco},{self.descricao}, {self.valor}, {self.rendimento})')
        conn.commit()

    def delInvestimentos(self):
        cursor.execute(f'DELETE FROM investimentos WHERE nome = "{self.nome}"')
        conn.commit()
    
    def listarInvestimentos(self):
        cursor.execute("SELECT * FROM investimentos")
        print(cursor.fetchall())