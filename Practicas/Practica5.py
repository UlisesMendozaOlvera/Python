#5 Manejo de información
"""Escribir una función que reciba n parámetros de llave valor e imprima la información en formato “{llave}”: “{Valor}”"""
d={};y="y"
def llave(**d):
    for key, value in d.items():
        print(f"Key : {key} , Valor: {value}")
while y=="y":
    a=input("Teclee una key :")
    b = input("Teclee un valor :")
    d[a] = b
    y=input("Agregar otro registro (y/n) :")
llave(**d)    
