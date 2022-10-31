from logger_base import log


class Persona:
    def __init__(self, id=None, nombre=None, edad=None, correo=None):
        self._id = id
        self._nombre = nombre
        self._edad = edad
        self._correo = correo
       

    def __str__(self):
        return f'''
            Id : {self._id}, nombre: {self._nombre},
            edad: {self._edad}, correo: {self._correo}
           
        '''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo
