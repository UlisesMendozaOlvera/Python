
#8.2.-Realizar un programa que contenga el siguiente menú

"""1. - Registro
2. - Inicio de sesión
3. - Salida
La opción de registro solicitara al usuario registrarse solicitando la información de los atributos la clase exceptuando el 
atributo Rol que por defecto será rol cliente, no se permitirán usuarios con CURP repetido en caso de mostrar mensaje de 
“El usuario ya existe” La opción de inicio de sesión permitirá al usuario introducir sus credenciales al ser correctas 
desplegar en pantalla la información del usuario de lo contrario mostrar mensaje de “datos incorrectos“"""
#8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la información de todos los usuarios registrados al momento.

from Practica8_1 import usuario
import os
def Registro():
    while True:
        os.system('cls')
        miObjeto=usuario()
        miObjeto.Usuario = input("Ingrese el nombre de Usuario : ")
        miObjeto.Contraseña = input("Ingrese una contraseña : ")
        miObjeto.Nombre = input("Ingrese su Nombre : ")
        miObjeto.CURP = input("Ingrese su CURP : ")
        miObjeto.Ciudad = input("Ingrese su ciudad : ")
        miObjeto.RegistrarUsuario()
        x=input("Desea registrar otro Usuario (y/n): ")
        if(x!="y"):break
    r = input("Desea ir al menu [y/n] : ")
    if r == "y":
        inicio()
def inicio():
    os.system('cls')
    opcion = int(input("1. - Registro  2. - Inicio de sesión  3. - Salida  : "))
    if opcion == 1:
        Registro()
    elif opcion == 2:
        while True:
            os.system('cls')
            miObjeto=usuario()
            print(miObjeto.Usuarios)
            miObjeto.Usuario=input("Usuario : ")
            miObjeto.Contraseña=input("Contraseña : ")
            if miObjeto.inicioSesion()==None:break
        r = input("Desea ir al menu [y/n] : ")
        if r == "y": inicio()
    elif opcion == 3:
        print("Salida")
    elif opcion != 1 or opcion != 2 or opcion != 3:
        print("Opcion no valida")
        inicio()
inicio()