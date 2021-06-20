from Commons.conexion_base import GetConexion
from GestionProductosModulo.entity.ProductoEntity import ProductoEntity
from Utils.Constantes import CODE_STATUS_QUERY
from Commons.logger_base import log

class ProductoDAO:

    @staticmethod
    def GetProductoByCategoria(idcat):
        cnx = GetConexion()
        if cnx != CODE_STATUS_QUERY['error_db']:
            try:
                with cnx:
                    with cnx.cursor() as cursor:
                        query = "select p.id, p.nombre,c.categorias,p.precio,p.stock from productos p inner join categorias c on p.fk_categorias = c.id where p.fk_categorias = %s"
                        params = [idcat]
                        lista_prod = []
                        cursor.execute(query, params)

                        for prod in cursor.fetchall():
                            objProd = ProductoEntity(id=prod[0], nombre=prod[1], nom_categoria=prod[2], precio=prod[3],
                                                     stock=prod[4])
                            lista_prod.append(objProd)
                        return lista_prod
            except Exception as err:
                log.error(f'error al realizar consulta en la bd: {err}')
                return CODE_STATUS_QUERY['error_query']
            finally:
                cursor.close()
                cnx.close()
        else:
            return CODE_STATUS_QUERY['error_db']