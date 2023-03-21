from connect.connectBD import conn, cursor

class Despesa:
    def __init__(self,nome, periodicidade, valor, categoria, data):
        self.periodicidade = periodicidade
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.nome = nome

        self.addDespesa()


    def addDespesa(self):
        cursor.execute(f"SELECT id FROM categoria WHERE nome = '{self.categoria}'")
        categoria_id = cursor.fetchall()[0][0]
        cursor.execute(f'INSERT INTO despesa (nome, data, categoria_id, periodicidade, valor) VALUES("{self.nome}", "{self.data}", {categoria_id},{self.periodicidade}, {self.valor})')
        conn.commit()

    def delDespesa(self):
        cursor.execute(f'DELETE FROM despesa WHERE nome = "{self.nome}" and data = {self.data} ')
        conn.commit()
    
    def listarDespesas(self):
        cursor.execute("SELECT * FROM despesa")
        print(cursor.fetchall())    

a = Despesa("Pica de borracha", 1600, 0, "comida", "24/01/2004")
a = Despesa("Pica de pedra", 1600, 0, "comida", "31/01/2004")
a = Despesa("Picanha", 1600, 0, "comida", "23/01/2004")
a = Despesa("Bolsa familia", 1600, 0, "comida", "13/01/2004")
