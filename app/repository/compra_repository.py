from app.database.connection import get_db
from app.models.compra_model import CompraModel

class CompraRepository:
    def get_all_compras(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT c.id, c.data_compra, c.cliente_nome, c.jogo_id, j.titulo, j.preco
            FROM compra c
            JOIN jogo j ON c.jogo_id = j.id
        """)
        rows = cursor.fetchall()
        compras = []
        for row in rows:
            compra = CompraModel(id=row[0], data_compra=row[1], cliente_nome=row[2], jogo_id=row[3])
            compra.jogo_titulo = row[4]
            compra.jogo_preco = row[5]
            compras.append(compra)
        return compras

    def get_compra_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM compra WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return CompraModel(id=row[0], data_compra=row[1], cliente_nome=row[2], jogo_id=row[3])
        return None

    def create_compra(self, compra: CompraModel):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO compra (data_compra, cliente_nome, jogo_id) VALUES (?, ?, ?)",
            (compra.get_data_compra(), compra.get_cliente_nome(), compra.get_jogo_id())
        )
        connection.commit()

    def update_compra(self, compra: CompraModel):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE compra SET data_compra = ?, cliente_nome = ?, jogo_id = ? WHERE id = ?",
            (compra.get_data_compra(), compra.get_cliente_nome(), compra.get_jogo_id(), compra.get_id())
        )
        connection.commit()

    def delete_compra(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM compra WHERE id = ?", (id,))
        connection.commit()
