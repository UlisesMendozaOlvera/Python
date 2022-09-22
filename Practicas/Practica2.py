#2 Manejo y manipulación de elementos de una lista
"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones 
múltiplos de 3, y muestre por pantalla la lista resultante."""
listaAbc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
listaAbcResultante = [listaAbc[i-1] for i in range(1,len(listaAbc)) if i % 3 != 0] #Muestra la lista resultante eliminando los multiplos de 3
print("Resultante :",listaAbcResultante)

#eliminadas = [listaAbc[i-1] for i in range(len(listaAbc), 1, -1) if i % 3 == 0]
#eliminadas.reverse()  # Lista de multiplos de 3

#print("Eliminados multiplos de 3 :",eliminadas)

