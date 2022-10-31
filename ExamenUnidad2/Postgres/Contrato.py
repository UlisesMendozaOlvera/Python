from logger_base import log

class Contrato:
    def __init__(self, id=None, no_contrato=None, costo=None, fecha_inicio=None, fecha_fin=None):
        self._id = id
        self._no_contrato = no_contrato
        self._costo = costo
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        

    def __str__(self):
        return f'''
            Id : {self._id}, No contrato: {self._no_contrato},
            costo: {self._costo}, Fecha de inicio: {self._fecha_inicio}
            Fecha fin : {self._fecha_fin}
        '''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def no_contrato(self):
        return self._no_contrato

    @no_contrato.setter
    def no_contrato(self, no_contrato):
        self._no_contrato = no_contrato

    @property
    def costo(self):
        return  self._costo

    @costo.setter
    def costo(self, costo):
        self._costo = costo

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio
    
    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin
