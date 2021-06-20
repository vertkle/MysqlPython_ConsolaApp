class CategoriaEntity:
    def __init__(self, id, nom_categoria):
        self.__id = id
        self.__nom_categoria = nom_categoria

    @property
    def getId(self):
        return self.__id
    @getId.setter
    def setId(self, id):
        self.__id = id

    @property
    def getNomCategoria(self):
        return self.__nom_categoria
    @getNomCategoria.setter
    def setNomCategoria(self, nom_categoria):
        self.__nom_categoria = nom_categoria

