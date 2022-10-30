import psycopg2 as bd
from logger_base import log
from psycopg2 import pool
import sys
class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD='bumo'
    _DBPORT='5432'
    _HOST='127.0.0.1'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON, cls._MAX_CON, host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD, port=cls._DBPORT, database=cls._DATABASE)
                log.debug(f'Creacion del pool {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error en el pool {e}')
                sys.exit()
        else:
            return cls._pool
    # end def

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(Conexion)
        log.debug(f'Conexion regresada : {conexion}')
    # end def
    @classmethod
    def cerrarConexiones(cls):
       cls.obtenerPool().closeall()
if __name__=='__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
