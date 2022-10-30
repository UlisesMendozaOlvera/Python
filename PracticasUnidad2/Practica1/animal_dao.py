from conexion import Conexion
from cursor_del_pool import CursorDelPool
from animal import Animal
from logger_base import log


class AnimalDAO:
   
    _SELECCIONAR = 'SELECT * FROM animal ORDER BY id_animal'
    _INSERTAR = 'INSERT INTO animal(nombre, edad, grupo_pertenece, tipo_alimentacion, habitat) VALUES(%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE animal SET nombre=%s, edad=%s, grupo_pertenece=%s, tipo_alimentacion=%s, habitat=%s WHERE id_animal=%s'
    _ELIMINAR = 'DELETE FROM animal WHERE id_animal=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            animals = []
            for registro in registros:
                animal = Animal(
                    registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                animals.append(animal)
            return animals

    @classmethod
    def insertar(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.nombre, animal.edad,
                       animal.grupo_pertenece, animal.tipo_alimentacion, animal.habitat)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'animal insertado: {animal}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.nombre, animal.edad, animal.grupo_pertenece,
                       animal.tipo_alimentacion, animal.habitat, animal.id_animal)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'animal actualizado: {animal}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.id_animal,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {animal}')
            return cursor.rowcount
