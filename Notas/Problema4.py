caracteres = {}
cadena = input('Introduce una cadena > ')
text=cadena.split()
print(text)
def dicc(cadena):
    
     for w in cadena:
        

for c in cadena:
    caracteres[c] = caracteres.get(c, 0) + 1

print('\n'.join([f'{k}: {v}' for k, v in caracteres.items()]))
