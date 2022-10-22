def mayor(a,b):
    a=str(a)
    b=str(b)
    a = ''.join(reversed(a))
    b = ''.join(reversed(b))
    may=""
    if a>b:
        may=a
    elif b>a:
        may=b
    print("Salida : ",may)

x=input("Teclee el primer numero :")
y=input("Teclee el segundo numero :")
mayor(x,y)