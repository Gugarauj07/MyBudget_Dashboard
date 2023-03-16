from connect.connectBD import conn, cursor

class Metas:
    def __init__(self, nome, descricao, valorestimado, dataInical, dataFinal):
        self.nome = nome
        self.descricao = descricao
        self.valorEstimado = valorestimado
        self.dataInical = dataInical
        self.dataFinal = dataFinal

    def addMetas(self):
        cursor.execute(f'INSERT INTO metas (nome, dataInicial, dataFinal, descricao, valorEstimado) VALUES("{self.nome}", "{self.dataInical}", "{self.dataFinal}","{self.descricao}", {self.valorEstimado})')
        conn.commit()

    def delMetas(self):
        cursor.execute(f'DELETE FROM metas WHERE nome = "{self.nome}"')
        conn.commit()
    
    def listarMetas(self):
        cursor.execute("SELECT * FROM metas")
        print(cursor.fetchall())