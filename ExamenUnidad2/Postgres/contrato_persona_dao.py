from conexion import Conexion
from cursor_del_pool import CursorDelPool
from contrato_persona import Contrato_persona
from logger_base import log


class contrato_personaDAO:

    _SELECCIONAR = 'SELECT * FROM contrato_persona '
    _INSERTAR = 'INSERT INTO contrato_persona(id_persona, id_contrato) VALUES(%s, %s)'
   
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contrato_personas = []
            for registro in registros:
                contrato_persona = Contrato_persona(
                    registro[0], registro[1], registro[2])
                contrato_personas.append(contrato_persona)
            return contrato_personas

    @classmethod
    def insertar(cls, contrato_persona):
        with CursorDelPool() as cursor:
            valores = (contrato_persona.id_persona, contrato_persona.id_contrato)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'contrato_persona insertado: {contrato_persona}')
            return cursor.rowcount

    