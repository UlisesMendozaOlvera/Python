from conexion import Conexion
from cursor_del_pool import CursorDelPool
from Contrato import Contrato
from logger_base import log

class ContratoDAO:
    
    _SELECCIONAR = 'SELECT * FROM contrato ORDER BY id'
    _INSERTAR = 'INSERT INTO contrato(no_contrato, costo, fecha_inicio, fecha_fin) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE contrato SET no_contrato=%s, costo=%s, fecha_inicio=%s, fecha_fin=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM contrato WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for registro in registros:
                contrato = Contrato(registro[0], registro[1], registro[2], registro[3], registro[4])
                contratos.append(contrato)
            return contratos

    @classmethod
    def insertar(cls, contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.no_contrato, contrato.costo, contrato.fecha_inicio, contrato.fecha_fin)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'contrato insertado: {contrato}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.no_contrato, contrato.costo, contrato.fecha_inicio, contrato.fecha_fin, contrato.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'contrato actualizado: {contrato}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.id,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {contrato}')
            return cursor.rowcount

