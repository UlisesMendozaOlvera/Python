#Modulos
#Existen modulos que no estan instalados en python 
import random 
numRamdom=random.randint(1,100)

while True:
    numero =int(input("Adivine el numero entre 1 y 100 : "))
    if numero==numRamdom:
        break
    if numero>numRamdom:
        print("El numero es menor")
    else:
        print("El numeor es mayor ")
print(f"el numero es : {numRamdom}")