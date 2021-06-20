from GestionProductosModulo.application.CategoriaApp import CategoriaApp
from GestionProductosModulo.application.ProductoApp import ProductoApp
from Commons.logger_base import log

isFirstTime = True
while True:
    try:
        # Imprimiendo las categorias
        if isFirstTime:
            CategoriaApp.ImprimirCategorias()
            isFirstTime = False

        # solicitando al usuario ingrese el id del producto
        idcat = int(input("Ingrese el id de la categoria, para ver los productos: "))

        # Verificar si el codigo que ingresa el usuario es para cerrar el sistema
        if CategoriaApp.IsCodeCloseSystem(idcat):
            print("Cerrando... Gracias...")
            break

        # imprimiendo el resultado de productos por categoria
        ProductoApp.ImprimirProductosByCategoria(idcat)
    except Exception as err:
        log.error(f'error en ejecucion del programa: {err}')
