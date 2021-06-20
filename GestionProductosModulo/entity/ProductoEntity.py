class ProductoEntity:
    def __init__(self, id=None, nombre=None, fk_categoria=None,nom_categoria=None, precio=None, stock=None):
        self.__id = id
        self.__nombre = nombre
        self.__fk_categoria = fk_categoria
        self.__nom_categoria = nom_categoria
        self.__precio = precio
        self.__stock = stock

    @property
    def getId(self):
        return self.__id
    @getId.setter
    def setId(self, id):
        self.__id = id

    @property
    def getNombre(self):
        return self.__nombre
    @getNombre.setter
    def setNombre(self, nombre):
        self.__nombre = nombre

    @property
    def getFkCategoria(self):
        return self.__fk_categoria
    @getFkCategoria.setter
    def setFkCategoria(self, fk_categoria):
        self.__fk_categoria = fk_categoria

    @property
    def getNomCategoria(self):
        return self.__nom_categoria

    @getNomCategoria.setter
    def setNomCategoria(self, nom_categoria):
        self.__nom_categoria = nom_categoria

    @property
    def getPrecio(self):
        return self.__precio

    @getPrecio.setter
    def setPrecio(self, precio):
        self.__precio = precio

    @property
    def getStock(self):
        return self.__stock

    @getStock.setter
    def setStock(self, stock):
        self.__stock = stock