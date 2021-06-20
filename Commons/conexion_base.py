from Commons.logger_base import log
import mysql.connector as con
from Utils.Constantes import CREDENCIALES_DB, CODE_STATUS_QUERY


def GetConexion(user='NN'):
    try:
        return con.connect(user=CREDENCIALES_DB['USER'], password=CREDENCIALES_DB['PASSWORD'], host=CREDENCIALES_DB['HOST'], database=CREDENCIALES_DB['DB_NAME'])
    except con.Error as err:
        log.error(f'error conectando a la base de datos: {err} by: {user}')
        return CODE_STATUS_QUERY['error_db']
