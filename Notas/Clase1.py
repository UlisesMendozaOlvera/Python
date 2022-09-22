#Tipos de Datos 
#Numericos Enteros



from operator import index
from pickle import LONG
from sre_constants import RANGE


x=0
y=1
z=-1
#print(x,y,z,end=";")
#print(type(x),y,z,end=";")
print(x,y,z,type(x),type(y),type(z),id(x),id(y),id(z))

#Flotantes
x=0.0
y=1.5
z=3.5
print(x,y,z,type(x),type(y),type(z),id(x),id(y),id(z))

#Complejos
x=5j
y=214j
z=90
print(x,y,z,type(x),type(y),type(z),id(x),id(y),id(z))

flotanteEntero=2.5
enteroFlotante=5
flotenteComplejo=4.0

flotanteEntero=int(flotanteEntero)
enteroFlotante=float(enteroFlotante)
flotenteComplejo=complex(flotenteComplejo)

print(flotanteEntero, enteroFlotante , flotenteComplejo)

#Booleanos
#Regresa falso si X no es igual que Y 
x=5
y=10
print(bool(x==y))
#Regresa falso si x es None(Null)
x=None
print(bool(x))
#Regresa falso si x es una secuencia vacia
x=()
print(bool(x))

#Cedenas 
#saludo="Buenos dias"
saludo="""Buenos Dias 
Hoy es Lunes"""
despedida="Adios"
print(f"saludos : {saludo}")
print(f"""saludos : {saludo}
Despedia : {despedida}""")

print(despedida[::-1])

#Tupla
tupla=(1,2,3)

#Listas
lista=[1,"Hola",3.67,[1,2,3]]
print(lista[3])
del lista[1] #Elimina un elemeto de la lista
l=[1,2,3,[4,5,6,[7,8,9]]]
print(l[3][2]) #6
print(l[3][3][2]) #9
for lista in enumerate(lista):
    print(index,lista)

for l,lista in zip(l,lista):
    print(l,lista)


#Diccionarios 
d = {"Love Actually" : "Richard Curtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

print(d["Kill Bill"])

d1={"Nombre":"Rocio","Edad":24,"Documento":"02344"}
d2=dict([("Nomre","Rocio"),("Edad",24)])
d3=dict(Nombre="Rocio",Edad=24,Documento="94853")
print(d3.get("Nombre"))
d3["Nombre"]="Pedro"
d3["Comida"]="Tacos"

for x in d1:
    print(d1[x])
for x,y in d3.items():
    print(x,y)

d4={"d1":d1,"d2":d2}

print(d4)


#GET
print(d3.get("d2"),"No encontrado")

#items
print(list(d3.items())[0])

#keys
print(d3.keys())
print(list(d3.keys())[0])
print(d3.values())
d3.popitem()
print(d3)

#update
a1={"a":1,"b":2}
a2={"a":100,"b":200}
a1.update(a2)
print(a1)
#Control De Flujo 
#Sentencias Condicionales

#IF
fav = "mundogeek.net"
# si (if) fav es igual a “mundogeek.net”
if fav == "mundogeek.net":
    print("Tienes buen gusto!")
    print("Gracias")

#IF ELSE
if fav == "mundogeek.ne":
    print("Tienes buen gusto!")
    print("Gracias")
else:
    print("Vaya, que lástima")    

#if … elif … elif … else
numero= 3
if numero < 0:
    print("Negativo")
elif numero > 0:
    print("Positivo")
else:
    print("Cero")

#A if C else B
var = print("par") if (numero % 2 == 0) else print("impar")

#Metodos SET
# Los SET no tienen indice, el indice es el valor mismo contenido dentro del SET
s = {1, 2, 3}
s.add(4)
print(s)
s.remove(5)
s.discard(5)
s.pop()  # Elimina un elemento aleatorio del SET

s.clear()
print(s)
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))
print(s1.intersection(s2))

#Bucles

#While

#Funciones


def f(x):
    print(2*x)

#f(5)


def suma(a, b):
    print(a+b)

#suma(5,2)
#suma(b=3,a=4)


def resta(a, b, c=0):
    print(a-b-c)

#resta(3,4)


listaNombres = ["rosa", "juan", "pedro"]


def nombre(*nombres):  # Convierte los parametros recividos en una tupla
    for n in nombres:
        print(n)


def suma(**suma):  # Convierte parametros en un diccionario
    for key, value in suma:
        print(key, value)

#nombre(listaNombres)
#nombre("rosa","juan","pedro")
#suma(a=3,b=4,c=2)


d1 = {"a": 2, "c": 3}
#suma(**d1) #Toma los valores de un diccionario


def sumaMedia(a, b, c):
    suma = a+b+c
    media = suma/3
    return suma, media


sumaResultado, mediaResultado = sumaMedia(1, 2, 3)
#print(sumaResultado, mediaResultado)


# no forza a recibir parametros de tipo int o de algun valor
def miFuncion(a: int, b: int) -> int:
    """
    Mi funcion comentada 
    """

#miFuncion()

#help(miFuncion) #
#print(miFuncion.__doc__) #


def suma3():
    x = 0
    while x <= 100:
        x += x

        print(x)


suma3()

#lambda arguments: espression


(lambda a, b: print(a+b))(1, 2)
def suma(a, b): return print(a+b)


suma(1, 3)
(lambda *n: print(sum(n)))(*list(range(0, 101, 1)))


def multiplicador(n):
    return lambda a: print(a*n)


duplicador = multiplicador(2)
triplicador = multiplicador(3)
duplicador(11)
triplicador(11)

#Input
x = int(input("Captura un numero: "))
print(x)

#tryCatch
try:
    pass
except TypeError:
    pass
except ZeroDivisionError:
    pass
except Exception as s:
    print(s)
else:
    pass
finally:
    pass

#assert
assert (1 == 2)


def suma(a, b):
    assert (type(a) == int)
    assert (type(b) == int)
    print(a+b)


suma(3, 3.2)


def factorial(n):
    """ Calcula el factorial de n.
    Pre: n debe ser un entero, mayor igual a 0
    Post: se devuelve el valor del factorial pedido
    """
    assert n >= 0, "n debe ser mayor igual a 0"
    fact = 1
    for i in RANGE(2, n+1):
        fact *= i
    return fact

#Validación de cadenas
"""Algunos de los métodos más utilizados para validar cadenas son:

isalnum() Devuelve True si la cadena es alfanumérica, de lo contrario False."""
cadena_alfanumerica = "El valor es 1000"
cadena_alfanumerica.isalnum()
False
cadena_alfanumerica = "awlpftawnju8mke4r5i9cfaw"
cadena_alfanumerica.isalnum()
True

"""
isalpha() Devuelve True si la cadena es alfabética, de lo contrario False. 
isdigit() Devuelve True si la cadena es numérica, de lo contrario False.
isspace Devuelve True si la cadena contiene solamente espacios en blanco, de lo contrario False.
"""
i=0
#Comprobaciones por tipo
if type(i) != int:
    raise TypeError, print("i debe ser del tipo int")

if type(i) not in (int, float, LONG, complex):
    raise TypeError, print("i debe ser numérico")

"""¿Qué es el método sort() en Python?
Este método toma una lista y le otorga un orden determinado. Dicho método no posee un valor de retorno.

En este ejemplo, tenemos una lista de números y podemos usar el método sort() para ordenar la lista de forma ascendente."""

mi_lista = [67, 2, 999, 1, 15]

# esto imprime la lista NO ordenada
print("Lista desordenada: ", mi_lista)

# Ordenemos la lista
mi_lista.sort()

# aquí tendremos la lista ordenada
print("Lista Ordenada: ", mi_lista)

"""El método sort() puede tomar dos argumentos opcionales llamados key y reverse.

key  tiene el valor de la función que será llamada en cada ítem de la lista.
En este ejemplo, podemos usar la función len() cómo el valor para el argumento key. key = len 
indicarán al programa ordenar la lista de nombres por longitud, del más pequeño al más largo."""

nombres = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]

print("Desordenado: ", nombres)
nombres.sort(key=len)
print("Ordenado: ", nombres)


"""En este ejemplo, tenemos una cadena dividida en palabras individuales, usando el métodosplit().
 A continuación empleamos el método sorted() para ordenar las palabras por longitud(es decir, el número de letras), 
 de menor a mayor.
"""
enunciado = "Encontré un dólar en la calle"

print("enunciado original: ", enunciado)
print(sorted(enunciado.split(), key=len))

#Estudiantes en orden de edad, de menor a mayor.
Estudiantes = [
    ('Daniela', 19, 'Clarinete'),
    ('María', 18, 'Arpa'),
    ('José', 20, 'Piano')
]
print(sorted(Estudiantes, key=lambda estudiante: estudiante[1]))

#Orden alfabético inverso por instrumento.
Estudiantes = [
    ('Daniela', 19, 'Clarinete'),
    ('María', 18, 'Arpa'),
    ('José', 20, 'Piano')
]

print(sorted(Estudiantes, key=lambda estudiante: estudiante[2], reverse=True))
