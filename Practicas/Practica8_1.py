#8 Resumen y multi-solución
"""8.1.-Definir una clase usuario que contenga como atributos:
Usuario
Contraseña
Rol
Nombre
CURP
Ciudad"""
import os
class usuario:
    Administradores = {"Usuario": "Admin", "Contraseña": "1234", "Rol": "Adminitrador",
                            "Nombre": "Bryan Mendoza", "CURP": "CSCFSF232dd", "Ciudad": "Nuevo Laredo"}
    Usuarios = {"Admin": Administradores}
    listaCURP = []
    def __init__(self) -> None:
        self.Usuario=""
        self.Contraseña=""
        self.Rol="cliente"
        self.Nombre=""
        self.CURP=""
        self.Ciudad=""
        self.DiccionarioUsuario = {}    
    def RegistrarUsuario(self):
        igual=False
        for l in self.listaCURP:
            if self.CURP == l:
                igual = True
        if igual==False:
            self.DiccionarioUsuario = {'Usuario': self.Usuario, 'Contraseña': self.Contraseña,
                                       'Rol': self.Rol, 'Nombre': self.Nombre, 'CURP': self.CURP, 'Ciudad': self.Ciudad}
            self.listaCURP.append(self.CURP)
            self.Usuarios[self.Usuario] = self.DiccionarioUsuario
            print(self.DiccionarioUsuario)
            print(self.Usuarios)
        elif igual==True:
            print
            print("             El Usuario ya existe ")
            print
    def inicioSesion(self):
        encontrado=False
        su=False
        res=False
        if self.Usuario in self.Usuarios:
                for key,value in self.Usuarios[self.Usuario].items():
                    if key=="Contraseña" and self.Contraseña==value:
                        encontrado=True
                        res=encontrado
                    if value=="Admin":su=True
        else:
            print("             Datos incorrectos | Usuario no existe")
            os.system("pause")
            return res
        if self.Usuario in self.Usuarios and encontrado==True:
            if su==True:
                os.system('cls')
                print('                                              Lista de Usuarios')
                for clave, valor in self.Usuarios.items():
                    print(f"Usuario: {clave} Rol : {valor['Rol']}  Nombre : {valor['Nombre']} CURP : {valor['CURP']} Ciudad : {valor['Ciudad']}")
            else:
                os.system('cls')
                print("               Datos del Usuario ")
                for key, value in self.Usuarios[self.Usuario].items():
                    print(" ")
                    print(key.title()+' : ',value)
    
        elif self.Usuario in self.Usuarios and encontrado != True:
            print("             Datos incorrectos | Contraseña incorrecta !")
            os.system("pause")
            return res