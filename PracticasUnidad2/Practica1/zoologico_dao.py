from conexion import Conexion
from cursor_del_pool import CursorDelPool
from zoologico import Zoologico
from logger_base import log


class ZoologicoDAO:

    _SELECCIONAR = 'SELECT * FROM zoologico ORDER BY id_zoologico'
    _INSERTAR = 'INSERT INTO zoologico(nombre, direccion, cantidad_animales, cantidad_guias, cantidad_cuidadores) VALUES(%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE zoologico SET nombre=%s, direccion=%s, cantidad_animales=%s, cantidad_guias=%s, cantidad_cuidadores=%s WHERE id_zoologico=%s'
    _ELIMINAR = 'DELETE FROM zoologico WHERE id_zoologico=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            zoologicos = []
            for registro in registros:
                zoologico = Zoologico(
                    registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                zoologicos.append(zoologico)
            return zoologicos

    @classmethod
    def insertar(cls, zoologico):
        with CursorDelPool() as cursor:
            valores = (zoologico.nombre, zoologico.direccion,
                       zoologico.cantidad_animales, zoologico.cantidad_guias, zoologico.cantidad_cuidadores)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'zoologico insertado: {zoologico}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, zoologico):
        with CursorDelPool() as cursor:
            valores = (zoologico.nombre, zoologico.direccion, zoologico.cantidad_animales,
                       zoologico.cantidad_guias, zoologico.cantidad_cuidadores, zoologico.id_zoologico)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'zoologico actualizado: {zoologico}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, zoologico):
        with CursorDelPool() as cursor:
            valores = (zoologico.id_zoologico,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {zoologico}')
            return cursor.rowcount
