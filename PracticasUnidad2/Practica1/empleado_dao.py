from conexion import Conexion
from cursor_del_pool import CursorDelPool
from empleado import Empleado
from logger_base import log

class EmpleadoDAO:
    
    _SELECCIONAR = 'SELECT * FROM empleado ORDER BY id_empleado'
    _INSERTAR = 'INSERT INTO empleado(nombre, apellido, edad, direccion, telefono) VALUES(%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre=%s, apellido=%s, edad=%s, direccion=%s, telefono=%s WHERE id_empleado=%s'
    _ELIMINAR = 'DELETE FROM empleado WHERE id_empleado=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            empleados = []
            for registro in registros:
                empleado = Empleado(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                empleados.append(empleado)
            return empleados

    @classmethod
    def insertar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.nombre, empleado.apellido, empleado.edad, empleado.direccion, empleado.telefono)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Empleado insertado: {empleado}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.nombre, empleado.apellido, empleado.edad, empleado.direccion, empleado.telefono, empleado.id_empleado)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Empleado actualizado: {empleado}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.id_empleado,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {empleado}')
            return cursor.rowcount

