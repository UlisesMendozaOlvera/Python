from conexion import Conexion
from cursor_del_pool import CursorDelPool
from Persona import Persona
from logger_base import log


class personaDAO:

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id'
    _INSERTAR = 'INSERT INTO persona (nombre, edad, correo) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, edad=%s, correo=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(
                    registro[0], registro[1], registro[2], registro[3], registro[4])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.edad,
                       persona.correo)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'persona insertado: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.edad,
                       persona.correo, persona.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'persona actualizado: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount
