class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None,edad=None) -> None:
        self._id_persona=id_persona
        self._nombre=nombre
        self._apellido=apellido
        self._email=email
        self._edad=edad
    def __str__(self) -> str:
        pass