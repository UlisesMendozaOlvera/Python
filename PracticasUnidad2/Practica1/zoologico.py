from logger_base import log


class Zoologico:
    def __init__(self, id_zoologico=None, nombre=None, direccion=None, cantidad_animales=None, cantidad_guias=None, cantidad_cuidadores=None):
        self._id_zoologico = id_zoologico
        self._nombre = nombre
        self._direccion = direccion
        self._cantidad_animales = cantidad_animales
        self._cantidad_guias = cantidad_guias
        self._cantidad_cuidadores = cantidad_cuidadores

    def __str__(self):
        return f'''
            Id zoologico: {self._id_zoologico}, Nombre: {self._nombre},
            direccion: {self._direccion}, cantidad de animales: {self._cantidad_animales}
            cantidad de guias: {self._cantidad_guias}, cantidad de cuidadores: {self._cantidad_cuidadores}
        '''

    @property
    def id_zoologico(self):
        return self._id_zoologico

    @id_zoologico.setter
    def id_zoologico(self, id_zoologico):
        self._id_zoologico = id_zoologico

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def cantidad_animales(self):
        return self._cantidad_animales

    @cantidad_animales.setter
    def cantidad_animales(self, cantidad_animales):
        self._cantidad_animales = cantidad_animales

    @property
    def cantidad_guias(self):
        return self._cantidad_guias

    @cantidad_guias.setter
    def cantidad_guias(self, cantidad_guias):
        self._cantidad_guias = cantidad_guias

    @property
    def cantidad_cuidadores(self):
        return self._cantidad_cuidadores

    @cantidad_cuidadores.setter
    def cantidad_cuidadores(self, cantidad_cuidadores):
        self._cantidad_cuidadores = cantidad_cuidadores
