#7 Formateo y conversiones
"""Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir YYYY/MM/DD” 
la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha del día de hoy en el formato seleccionado."""
from datetime import datetime
hora=datetime.now()
opcion = int(input("1.- Imprimir YYYY/MM/DD  2.- Imprimir MM/DD/YYYY  : "))
if opcion==1:
    print(hora.strftime("%Y-%m-%d"))
elif opcion==2:
    print(hora.strftime("%m-%d-%Y"))
elif opcion!=1 or opcion!=2:
    print("Opcion no valida")