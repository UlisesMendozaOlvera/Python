from logger_base import log

class Empleado:
    def __init__(self, id_empleado=None, nombre=None, apellido=None,edad=None, direccion=None, telefono=None):
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._direccion = direccion
        self._telefono = telefono

    def __str__(self):
        return f'''
            Id Empleado: {self._id_empleado}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Edad: {self._edad}
            Direccion: {self._direccion}, Telefono: {self._telefono}
        '''

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return  self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono
