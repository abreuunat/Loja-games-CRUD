class JogoModel:
    def __init__(self, id, titulo, genero, plataforma, preco):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__plataforma = plataforma
        self.__preco = preco

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def get_plataforma(self):
        return self.__plataforma

    def get_preco(self):
        return self.__preco
