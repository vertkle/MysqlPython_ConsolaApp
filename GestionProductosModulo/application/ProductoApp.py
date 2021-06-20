from GestionProductosModulo.dao.ProductoDAO import ProductoDAO

class ProductoApp:

    @staticmethod
    def GetProductosByCategoria(idcat):
        return ProductoDAO.GetProductoByCategoria(idcat)

    @staticmethod
    def ImprimirProductosByCategoria(idcat):
        print("="*70)
        lista = ProductoApp.GetProductosByCategoria(idcat)
        if len(lista) > 0:
            print("""ID     NOMBRE      CATEGORIA       PRECIO      STOCK""")
            for prod in ProductoApp.GetProductosByCategoria(idcat):
                print(
                    f"""{prod.getId}     {prod.getNombre}       {prod.getNomCategoria}         {prod.getPrecio}      {prod.getStock}""")
        else:
            print("NO SE ENCONTRARON PRODUCTOS EN ESTA CATEGORIA")
        print("=" * 70)