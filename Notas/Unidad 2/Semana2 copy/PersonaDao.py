from Clases import Persona
from Conexion import Conexion
from logger_base import log
from CursorDelPool import CursorDelPool

class PersonasDao:
    _SELECCIONAR=   "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR="INSERT INTO persona(nombre,apellido,email, edad ) Values(%s,%s,%s,%s)"
    _ACTUALIZAR="UPDATE persona SET nombre=%s,apellido=%s,email=%s, edad=%s WHERE id_persona=%s"
    _ELIMINAR="DELETE FROM persona WHERE id_persona=%s"
    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros=cursor.fetchall()
                personas=[]
                for r in registros:
                    persona=Persona(r[0],r[1],r[2],r[3],r[4])
                    personas.append(persona)
                return personas
    # end def
    @classmethod
    def actualizar(cls,Persona):
        with CursorDelPool() as cursor:
                valores=(Persona.Nombre,Persona.Apellido,Persona.Email,Persona.Edad)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount
                # end def
    @classmethod
    def insertar(cls):
        with CursorDelPool() as cursor:
                valores=(Persona.Nombre,Persona.Apellido,Persona.Email,Persona.Edad)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount
                # end def
    @classmethod
    def eliminar(cls):
        with CursorDelPool() as cursor:
            valores = (Persona.id_Persona,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
            # end def
if __name__=="__main__":
   #insertar 
    persona1=Persona(nombre="Pancrasio",apellido="Mendez",email="cccsdcc@gmail.com",edad=22)
    personasInsertadas=PersonasDao.insertar(persona1)
    log.debug(f"Personas Insertadas {personasInsertadas}")
   #Actualizar
    persona2 = Persona(id_persona=2,nombre="Pancrasio", apellido="Mendez",
                       email="cccsdcc@gmail.com", edad=22)
    personasActualizadas = PersonasDao.actualizar(persona2)
    log.debug(f"Personas Actualizadas {personasActualizadas}")
   #Eliminar
    persona3 = Persona(id_persona=2,)
    personasEliminadas = PersonasDao.eliminar(persona3)
    log.debug(f"Personas Eliminadas {personasEliminadas}")
   #ver
    persona=PersonasDao.seleccionar()
    for p in persona:
        log.debug(p)
    