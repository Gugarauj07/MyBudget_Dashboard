from connect.connectBD import conn, cursor

class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.id = None

    def loginUsuário(self):
        cursor.execute("SELECT login FROM usuario")
        listaLogin = [list[0] for list in cursor.fetchall()]
        if self.login in listaLogin:
            cursor.execute(f"SELECT senha, id FROM usuario WHERE login = '{self.login}'")
            senha, self.id = cursor.fetchall()[0]
            if senha == self.senha:
                return True
            else:
                print("Senha incorreta!")
        else:
            print("Login não consta do banco de dados!")


    def registrarUsuário(self):
        cursor.execute("SELECT login FROM usuario")
        listaLogin = [list[0] for list in cursor.fetchall()]
        if self.login not in listaLogin:
            cursor.execute(f'INSERT INTO usuario (nome, login, senha) VALUES("{self.nome}", "{self.login}", "{self.senha}")')
            conn.commit()
        else:
            print("Esse e-mail já está vinculado a um usuário")
    
    def deletarUsuário(self):
        cursor.execute(f'DELETE FROM usuario WHERE login = "{self.login}"')
        conn.commit()

    def listarUsuario(self):
        cursor.execute("SELECT * FROM usuario")
        print(cursor.fetchall())

Gu = Usuario("Ana", "gugara123@gmail.com", "aklsdla")
Gu.registrarUsuário()
Gu.loginUsuário()
print(Gu.id)