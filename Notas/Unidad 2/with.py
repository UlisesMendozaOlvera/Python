import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres", password="bumo", host="127.0.0.1", port="5432", database="prueba")
print(conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
            """sentencia = "SELECT * FROM persona WHERE id_persona=%s"
            idPersona = input("Proporcione un id de persona: ")
            cursor.execute(sentencia, (idPersona,))
            resultado = cursor.fetchone()
            print(resultado)
            """
            sentencia = "INSERT INTO usuarios.cliente(nombre, apellido, email) Values(%s,%s,%s)"
            valores = (('juan', 'perez', 23),
                       ('juan', 'arredondo', 23), 
                       ('juan', 'rivera', 23))
            cursor.executemany(sentencia,valores)
            #cursor.execute(sentencia, valores)
            #registroInsertado=cursor.rowcount
            #sentencia = "DELETE FROM persona WHERE id_persona=%s"
            #entrada=input(" Ingrese los IDs: ")
            #valores=(tuple())

           
except Exception as e:
   
    log.error(e)


finally:
    conexion.close()
