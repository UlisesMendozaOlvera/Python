#1 Funciones con n parámetros
#Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el producto total.
def sumar(*args):
	resultado = 0
	print("suma de :",args)
	for valor in args:
		resultado +=valor
	return resultado
print("Suma Total de n numeros : ",sumar(3,5,5,4,5,4,4))























