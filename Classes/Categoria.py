from connect.connectBD import conn, cursor

class Categoria:
    def __init__(self, nome, descricao):   
        self.nome = nome
        self.descricao = descricao

    def addCategoriaReceita(self):
        cursor.execute(f'INSERT INTO categoria (nome, descricao, tipo) VALUES("{self.nome}", "{self.descricao}", "receita")')
        conn.commit()

    def addCategoriaInvestimento(self):
        cursor.execute(f'INSERT INTO categoria (nome, descricao, tipo) VALUES("{self.nome}", "{self.descricao}", "investimento")')
        conn.commit()

    def delCategoria(self):
        cursor.execute(f'DELETE FROM categoria WHERE nome = "{self.nome}"')
        conn.commit()
    
    def listarCategorias(self):
        cursor.execute("SELECT * FROM categoria")
        print(cursor.fetchall())

Cat1 = Categoria("vendas", "porra")
Cat1.addCategoriaReceita()
Cat2 = Categoria("salário", "mensal")
Cat2.addCategoriaReceita()
Cat3 = Categoria("Renda fixa", "Tipo de investimento onde a renda é fixa")
Cat3.addCategoriaInvestimento()