from Clases import Persona
from Conexion import Conexion
from logger_base import log

class Personas:
    _SELECCIONAR=   "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR="INSERT INTO persona(nombre,apellido,email, edad ) Values(%s,%s,%s,%s)"
    _ACTUALIZAR="UPDATE persona SET nombre=%s,apellido=%s,email=%s, edad=%s WHERE id_persona=%s"
    _ELIMINAR="DELETE FROM persona WHERE id_persona=%s"
    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
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
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores=(Persona.Nombre,Persona.Apellido,Persona.Email,Persona.Edad)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount
                # end def
    @classmethod
    def insertar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores=(Persona.Nombre,Persona.Apellido,Persona.Email,Persona.Edad)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount
                # end def
if __name__=="__main__":
    Persona1=(Persona.Nombre,Persona.Apellido,Persona.Email,Persona.Edad)
    personas