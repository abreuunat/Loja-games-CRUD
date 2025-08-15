CREATE TABLE jogo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT NOT NULL,
    plataforma TEXT NOT NULL,
    preco REAL NOT NULL
);

CREATE TABLE compra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra DATE NOT NULL,
    cliente_nome TEXT NOT NULL,
    jogo_id INTEGER NOT NULL,
    FOREIGN KEY (jogo_id) REFERENCES jogo(id)
);
