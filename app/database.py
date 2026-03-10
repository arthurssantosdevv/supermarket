import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT,
        sku TEXT UNIQUE NOT NULL,
        custo REAL,
        estoque INTEGER DEFAULT 0,
        ativo BOOLEAN DEFAULT 1,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP);
               ''')


cursor.execute('''
        CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE,
        telefone TEXT,
        email TEXT,
        senha TEXT,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP);
               ''')

cursor.execute('''
        CREATE TABLE funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT,
        email TEXT UNIQUE,
        senha TEXT,
        ativo BOOLEAN DEFAULT 1,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP);
               ''')

cursor.execute('''
        CREATE TABLE caixas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        aberto_por INTEGER,
        aberto_em DATETIME,
        fechado_em DATETIME,

        FOREIGN KEY (aberto_por) REFERENCES funcionarios(id));
               ''')

cursor.execute('''
        CREATE TABLE vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        funcionario_id INTEGER,
        caixa_id INTEGER,
        total REAL,
        desconto REAL DEFAULT 0,
        data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id),
        FOREIGN KEY (caixa_id) REFERENCES caixas(id));
               ''')

conn.commit()
conn.close