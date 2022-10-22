import psycopg2 as bd
import sys
from logger_base import log


class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD='bumo'
    _DBPORT='5432'
    _HOST='127.0.0.1'

    _conexion=None
    _cursor=None

    @classmethod
    def ObtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion=bd.connect(host=cls._HOST,user=cls._USERNAME, password=cls._PASSWORD, port=cls._DBPORT, database=cls._DATABASE)
                log.debug(f"Conexion a BD : {cls._conexion}")
                return cls._conexion
            except Exception as e:
                log.error(f"Ocurrio un error : {e}")
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def ObtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor=cls.ObtenerConexion().cursor()
                log.debug(f"Conexion a BD : {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error(f"Ocurrio un error : {e}")
                sys.exit()
        else:
            return cls._cursor
if __name__=='__main__':
    Conexion.ObtenerConexion()
    Conexion.ObtenerCursor()