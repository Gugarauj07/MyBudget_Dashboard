from Categoria import Categoria, conn, cursor

class CategoriaDespesa(Categoria):
    def __init__(self, limite, prioridade, nome, descricao):   
        super().__init__(nome, descricao)
        self.limite = limite
        self.prioridade = prioridade

        self.addCategoriaDespesa()

    def addCategoriaDespesa(self):
        cursor.execute(f'INSERT INTO categoria (nome, descricao, tipo, limite, prioridade) VALUES("{self.nome}", "{self.descricao}", "despesa", "{self.limite}", "{self.prioridade}")')
        conn.commit()

cat1 = CategoriaDespesa(2000, "alta", "comida", "coisa pra comer")