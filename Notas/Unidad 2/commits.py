import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres", password="bumo", host="127.0.0.1", port="5432", database="prueba")
print(conexion)
try:
    conexion.autocommit=False
    cursor=conexion.cursor()
    sentencia="INSERT INTO usuarios.cliente(id_cliente, nombre, apellido, email) VALUES (%s, %s, %s, %s)" #Pasar valores por referencia 
    valores=(17100333,'Juan','Perez','bumo@gmail.com');
    cursor.execute(sentencia,valores)
    log.debug("Sentencia Insert")
    conexion.commit()
except Exception as e:
    conexion.rollback()
    log.error(e)
   
    
finally:
    conexion.close()
