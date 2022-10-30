from logger_base import log


class Animal:
    def __init__(self, id_animal=None, nombre=None, edad=None, grupo_pertenece=None, tipo_alimentacion=None, habitat=None):
        self._id_animal = id_animal
        self._nombre = nombre
        self._edad = edad
        self._grupo_pertenece = grupo_pertenece
        self._tipo_alimentacion = tipo_alimentacion
        self._habitat = habitat

    def __str__(self):
        return f'''
            Id Animal: {self._id_animal}, Nombre: {self._nombre},
            Edad: {self._edad}, Grupo al que pertenece: {self._grupo_pertenece}
            Tipo  de Alimentacion: {self._tipo_alimentacion}, Habitat: {self._habitat}
        '''

    @property
    def id_animal(self):
        return self._id_animal

    @id_animal.setter
    def id_animal(self, id_animal):
        self._id_animal = id_animal

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def grupo_pertenece(self):
        return self._grupo_pertenece

    @grupo_pertenece.setter
    def grupo_pertenece(self, grupo_pertenece):
        self._grupo_pertenece = grupo_pertenece

    @property
    def tipo_alimentacion(self):
        return self._tipo_alimentacion

    @tipo_alimentacion.setter
    def tipo_alimentacion(self, tipo_alimentacion):
        self._tipo_alimentacion = tipo_alimentacion

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, habitat):
        self._habitat = habitat
