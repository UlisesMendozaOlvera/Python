#4 Entrada de datos y estructuración.
"""Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture las materias 
y créditos de su semestre preferido(inferior a 8vo) al final imprimir en el formato “{asignatura}” tiene “{créditos}” 
créditos. Y la suma de todos los créditos del semestre"""
materias = {}
y = "y";aux = 0.0
while y=="y":
    asig=input("Teclee una asignatura : ");creditos=float(input("Teclee los creditos :"))
    materias[asig]=creditos
    y=input("Quiere Ingresar otra asignatura (y/n): ")
for key,value in materias.items():
    print(f"Asignatura: {key} , Creditos: {value}"); aux+=value
print("Total de creditos : ",aux)