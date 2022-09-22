#6 Razonamiento y prueba de código
"""Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, 
no utilizar condicionales, máximo 5 líneas de código."""
d={"1":"UNO","2":"DOS","3":"TRES","4":"CUATRO","5":"CINCO","6":"SEIS","7":"SIETE","8":"OCHO","9":"NUEVE","10":"DIEZ","11":"ONCE","12":"DOCE","13":"TRECE","14":"CATROCE","15":"QUINCE","16":"DIECISEIS","17":"DIECISIETE","18":"DIECIOCHO","19":"DIECINUEVE","20":"VEINTE"}
print("Teclee un numero del 0 al 20 : ");var = input();r=d.get(var);print(r) if (r != None) else print("El numero no esta en el rango")