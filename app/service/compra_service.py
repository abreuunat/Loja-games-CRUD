from app.repository.compra_repository import CompraRepository
from app.repository.jogo_repository import JogoRepository

class CompraService:
    def __init__(self):
        self.compra_repository = CompraRepository()
        self.jogo_repository = JogoRepository()

    def get_all_compras(self):
        return self.compra_repository.get_all_compras()

    def get_compra_by_id(self, id):
        compra = self.compra_repository.get_compra_by_id(id)
        if not compra:
            raise ValueError(f"Compra com ID {id} não encontrada.")
        return compra

    def create_compra(self, compra):
        self._validar_compra(compra)
        self.compra_repository.create_compra(compra)

    def update_compra(self, compra):
        if not self.compra_repository.get_compra_by_id(compra.get_id()):
            raise ValueError(f"Compra com ID {compra.get_id()} não existe.")
        self._validar_compra(compra)
        self.compra_repository.update_compra(compra)

    def delete_compra(self, id):
        if not self.compra_repository.get_compra_by_id(id):
            raise ValueError(f"Compra com ID {id} não existe.")
        self.compra_repository.delete_compra(id)

    def _validar_compra(self, compra):
        if not compra.get_cliente_nome():
            raise ValueError("O nome do cliente é obrigatório.")
        if not compra.get_data_compra():
            raise ValueError("A data da compra é obrigatória.")
        