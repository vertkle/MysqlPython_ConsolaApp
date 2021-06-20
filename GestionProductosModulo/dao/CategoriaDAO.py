from Commons.conexion_base import GetConexion
from GestionProductosModulo.entity.CategoriaEntity import CategoriaEntity
from Utils.Constantes import CODE_STATUS_QUERY
from Commons.logger_base import log


class CategoriaDAO:

    @staticmethod
    def GetAllCategoria():
        cnx = GetConexion()
        if cnx != CODE_STATUS_QUERY['error_db']:
            try:
                with cnx:
                    with cnx.cursor() as cursor:
                        lista_categoria = []
                        query = "select * from categorias"
                        cursor.execute(query)
                        for cat in cursor.fetchall():
                            objCat = CategoriaEntity(cat[0], cat[1])
                            lista_categoria.append(objCat)
                        return lista_categoria
            except Exception as err:
                log.error(f'error al realizar consulta en la bd: {err}')
                return CODE_STATUS_QUERY['error_query']
            finally:
                cursor.close()
                cnx.close()
        else:
            return CODE_STATUS_QUERY['error_db']


