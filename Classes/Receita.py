from connect.connectBD import conn, cursor

class Receita:
    def __init__(self, nome, valor, periodicidade, categoria, data):
        self.valor = valor
        self.periodicidade = periodicidade
        self.categoria = categoria
        self.data = data
        self.nome = nome
        
    def addReceita(self):
        cursor.execute(f"SELECT id FROM categoria WHERE nome = '{self.categoria}'")
        categoria_id = cursor.fetchall()[0][0]
        cursor.execute(f'INSERT INTO receita (nome, data, categoria_id, periodicidade, valor) VALUES("{self.nome}", "{self.data}", {categoria_id},{self.periodicidade}, {self.valor})')
        conn.commit()

    def delReceita(self):
        cursor.execute(f'DELETE FROM receita WHERE nome = "{self.nome}"')
        conn.commit()
    
    def listarReceitas(self):
        cursor.execute("SELECT * FROM receita")
        print(cursor.fetchall())

a = Receita("Salário", 1600, 1, "vendas", "24/01/2004")
a.addReceita()
a.listarReceitas()