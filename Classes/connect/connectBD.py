import sqlite3

conn = sqlite3.connect("budget-app.db")
cursor = conn.cursor()


cursor.execute("""
        create table if not exists usuario (
            id integer primary key autoincrement,
            nome text,
            login text,
            senha text
        )
        """)

cursor.execute("""
        create table if not exists categoria (
            id integer primary key autoincrement,
            nome text,
            descricao text,
            tipo text,
            limite integer,
            prioridade text,
            usuario_id integer,
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        )
        """)

cursor.execute("""
        create table if not exists receita (
            id integer primary key autoincrement,
            nome text,
            data DATE,
            periodicidade text,
            valor real,
            categoria_id integer,
            usuario_id integer,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        )
        """)

cursor.execute("""
        create table if not exists despesa (
            id integer primary key autoincrement,
            nome text,
            data DATE ,
            periodicidade text,
            valor real,
            categoria_id integer,
            usuario_id integer,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        )
        """)

cursor.execute("""
        create table if not exists metas (
            id integer primary key autoincrement,
            nome text,
            dataInicial DATE ,
            dataFinal DATE ,
            descricao text,
            valorEstimado real,
            usuario_id integer,
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        )
        """)

cursor.execute("""
        create table if not exists investimentos (
            id integer primary key autoincrement,
            nome text,
            data DATE,
            rendimentoANO integer,
            risco integer,
            descricao text,
            valor real,
            categoria_id integer,
            usuario_id integer,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        )
        """)
