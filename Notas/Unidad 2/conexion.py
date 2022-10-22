#pip install psycopg2

import psycopg2

conexion = psycopg2.connect(user="postgres",password="bumo",host="127.0.0.1",port="5432",database="postgres")
cursor=conexion.cursor()
cursor.execute("SELECT * FROM public.persona")
resultados=cursor.fetchall()
print(resultados)