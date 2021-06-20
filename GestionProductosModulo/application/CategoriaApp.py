from GestionProductosModulo.dao.CategoriaDAO import CategoriaDAO
from GestionProductosModulo.entity.CategoriaEntity import CategoriaEntity


class CategoriaApp:

    @staticmethod
    def GetAllCategoria():
        lista = CategoriaDAO.GetAllCategoria()
        idCloseSystem = lista[len(lista) - 1].getId + 1
        objCatLast = CategoriaEntity(idCloseSystem, f"SELECCIONE {idCloseSystem} PARA SALIR DEL PROGRAMA")
        lista.append(objCatLast)
        return lista

    @staticmethod
    def ImprimirCategorias():
        print("""ID         Categorias""")
        for cat in CategoriaApp.GetAllCategoria():
            print(f"""{cat.getId}         {cat.getNomCategoria}""")

    @staticmethod
    def IsCodeCloseSystem(idcatclose):
        lista = CategoriaApp.GetAllCategoria()
        idclose = lista[len(lista) - 1].getId
        return True if idcatclose == idclose else False
