#1 Cadenas 
#2 Funciones
"""cadena=input("Teclee una frase : ")

def convertir(c):
    l=c.split()
    d1={}
    for i in l:
        if i in l:
            d1[i]+=1
        else:
            d1[i]=1
    return d1

def f(d):
    palabra=""
    numero=0
    for pal,num in d.items():
        if num>numero:
            palabra=pal
            numero=num
    return palabra,numero

"""





#3 Tipos de Datos
#
# una  en dos de sus productos payasos y muñecas suele hacer hacer su venta por correo y la empresa de logistica, 
# les cobra por preso de paquete cada payaso pesa 112 cada muñeca 75 escribe el programa que leea 
#calcule el peso del paquete que sera enviado por cada 100g se cobra 2.50 pesos y por cada muñeca 2 pesos
"""
pesoPayaso=112
precioPayaso=2.5
pesoMuneca=75
precioMuneca=2

cantidadPayaso=int(input("Teclee la cantidad de payasos: "))
cantidadMuneca=int(input("Teclee la cantidad de Muñecas: "))
def Calcular(a,b):
        PesoTotalPayaso=a*pesoPayaso
        PrecioTotalPayaso=(PesoTotalPayaso/100)*precioPayaso
        PesoTotalMuneca=b*pesoMuneca
        PrecioTotalMuneca=(PesoTotalMuneca/100)*precioMuneca
        print("Payaso Peso :",PesoTotalPayaso,"Precio :",PrecioTotalPayaso)
        print("Muñeca Peso :",PesoTotalMuneca,"Precio :",PrecioTotalMuneca)
        print("Peso Total :",PesoTotalPayaso+PesoTotalMuneca)
        print("Precio Total :",PrecioTotalPayaso+PrecioTotalMuneca)


Calcular(cantidadPayaso, cantidadMuneca)
"""


"""Escribir un programa que pregunte el nombre de un producto su precio y un numero de unidades
y muestre en la pantalla  una cadena con el nombre del producto seguido de su precio unitario con 6 
digitos y el coste total con 8 digitos enteros a decimales """

"""def Cadenas():
    nombre=input("Inserte nombre del producto: ")
    precio=float(input("Inserte precio del producto :"))
    unidades=input("Inserte numero de unidades :")
    total=precio*unidades
    print("{nombre} {precio:6d.2f} {unidades:3d} {total:8.2f}".format{nombre=nombre,precio=precio,unidades=unidades,total=total})
"""
#4 Diccionarios
"""Escribir un programa que guarde en un diccionario las frutas en la tabla , pregunte al usuario por una fruta y numero de kilos 
si la fruta no esta en el diccionario debe mostrar un mensaje acerca de ello"""
frutas={"Platano":135,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
fruta=input("Teclee una fruta :")
kilos=input("Teclee los kilos :")
def r(f,k):
    print(frutas[f])
    
r(fruta,kilos)


#5 Listas y tuplas
"""Escribir un programa que almacene """
x={(1,2,3),(4,5,6)}
y={(-1,0),(0,0),(1,1)}
r=[[0,0],[0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            r[i][j]+=x[i][k]*y[k][j]

for i in range(len(r)):
    r[i]=list (r[i])
for i in r:
    print(i)


#6 Bucles
"""Escribir un programa que le pregunte al usuario por una frase y una letra y mostrar en pantalla el numero de veces que se 
repite en la letra en la frase """
#letra=input("Teclee una letra :")
#frase=input("Teclee una frase :")






#7 Condiccionales 
"""Una pizzeria ofrece comidas vegetarianas a sus clientes los ingredientes son pimiento y toffu 
ingredientes no vegetarianos peperoni, salmon y jamon Escribir un programa que pregunte al usuario si 
quiere una pizza vegetariana o no, en base a su respuesta que le muestre un menu en base sus ingredientes 
aparte de sus ingredientes seleccionados el tomate y el queso estan en todas las pizzas  el final debe mostrar todos los ingredientes"""