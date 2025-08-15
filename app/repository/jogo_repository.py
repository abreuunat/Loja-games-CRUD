from app.database.connection import get_db
from app.models.jogo_model import JogoModel

class JogoRepository:
    def get_all_jogos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM jogo")
        rows = cursor.fetchall()
        return [JogoModel(id=row[0], titulo=row[1], genero=row[2], plataforma=row[3], preco=row[4]) for row in rows]

    def get_jogo_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM jogo WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return JogoModel(id=row[0], titulo=row[1], genero=row[2], plataforma=row[3], preco=row[4])
        return None

    def create_jogo(self, jogo: JogoModel):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO jogo (titulo, genero, plataforma, preco) VALUES (?, ?, ?, ?)",
            (jogo.get_titulo(), jogo.get_genero(), jogo.get_plataforma(), jogo.get_preco())
        )
        connection.commit()

    def update_jogo(self, jogo: JogoModel):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE jogo SET titulo = ?, genero = ?, plataforma = ?, preco = ? WHERE id = ?",
            (jogo.get_titulo(), jogo.get_genero(), jogo.get_plataforma(), jogo.get_preco(), jogo.get_id())
        )
        connection.commit()

    def delete_jogo(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM jogo WHERE id = ?", (id,))
        connection.commit()
