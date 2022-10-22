from ast import While


def div(n,m):
    lista=[]
    while n>1:

        lista.append(n)
        n=n/m
        if n==1:
            lista.append(n)
    if n==1:
            print(lista)
    else:
            print("Secuencia Invalida")
    
x=int(input("Teclee un numero :"))
y = int(input("Teclee un otro numero :"))

div(x,y)