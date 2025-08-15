from app.repository.jogo_repository import JogoRepository

class JogoService:
    def __init__(self):
        self.jogo_repository = JogoRepository()

    def get_all_jogos(self):
        return self.jogo_repository.get_all_jogos()

    def get_jogo_by_id(self, id):
        jogo = self.jogo_repository.get_jogo_by_id(id)
        if not jogo:
            raise ValueError(f"Jogo com ID {id} não encontrado.")
        return jogo

    def create_jogo(self, jogo):
        self._validar_jogo(jogo)
        self.jogo_repository.create_jogo(jogo)

    def update_jogo(self, jogo):
        if not self.jogo_repository.get_jogo_by_id(jogo.get_id()):
            raise ValueError(f"Jogo com ID {jogo.get_id()} não existe.")
        self._validar_jogo(jogo)
        self.jogo_repository.update_jogo(jogo)

    def delete_jogo(self, id):
        if not self.jogo_repository.get_jogo_by_id(id):
            raise ValueError(f"Jogo com ID {id} não existe.")
        self.jogo_repository.delete_jogo(id)

    def _validar_jogo(self, jogo):
        if not jogo.get_titulo() or not jogo.get_titulo().strip():
            raise ValueError("O título do jogo é obrigatório.")
        if not jogo.get_genero() or not jogo.get_genero().strip():
            raise ValueError("O gênero do jogo é obrigatório.")
        if not jogo.get_plataforma() or not jogo.get_plataforma().strip():
            raise ValueError("A plataforma do jogo é obrigatória.")
        
        # Converte para float antes de validar
        try:
            preco = float(jogo.get_preco())
        except (ValueError, TypeError):
            raise ValueError("O preço do jogo deve ser um número válido.")
        
        if preco <= 0:
            raise ValueError("O preço do jogo deve ser maior que zero.")
