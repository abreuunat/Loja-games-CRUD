class CompraModel:
    def __init__(self, id, data_compra, cliente_nome, jogo_id):
        self.__id = id
        self.__data_compra = data_compra
        self.__cliente_nome = cliente_nome
        self.__jogo_id = jogo_id

    def get_id(self):
        return self.__id

    def get_data_compra(self):
        return self.__data_compra

    def get_cliente_nome(self):
        return self.__cliente_nome

    def get_jogo_id(self):
        return self.__jogo_id
