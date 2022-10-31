from logger_base import log



class Contrato_persona:
    def __init__(self, id_persona=None, id_contrato=None):
        self._id_persona = id_persona
        self._id_contrato = id_contrato
       
    def __str__(self):
        return f'''
            id_persona : {self._id_persona}, id_contrato: {self._id_contrato},
            
        '''

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def id_contrato(self):
        return self._id_contrato

    @id_contrato.setter
    def id_contrato(self, id_contrato):
        self._id_contrato = id_contrato
