from animal_dao import AnimalDAO
from empleado import Empleado
from empleado_dao import EmpleadoDAO
from animal import Animal
from animal_dao import AnimalDAO
from zoologico import Zoologico
from zoologico_dao import ZoologicoDAO
from logger_base import log
import os

opcion=None
while opcion != 5:
    os.system('cls')
    print('Opciones CRUD: ')
    print('1. Empleados')
    print('2. Animales')
    print('3. Zoologico')
    print('4. Salir')
    opcion = int(input('Escribe tu opcion (1-4): '))
    if opcion==1:
        os.system('cls')
        opcion = None
        while opcion != 5:
            print('Opciones:')
            print('1. Listar Empleados')
            print('2. Agregar Empleados')
            print('3. Modificar Empleados')
            print('4. Eliminar Empleados')
            print('5. Salir')
            opcion = int(input('Escribe tu opcion (1-5): '))
            if opcion == 1:
                empleados = EmpleadoDAO.seleccionar()
                for empleado in empleados :
                    log.info(empleado)
            elif opcion == 2:
                nombre_var = input('Escribe el nombre: ')
                apellido_var = input('Escribe el apellido: ')
                edad_var = int(input('Escribe el edad: '))
                direccion_var = input('Escribe la direccion: ')
                telefono_var = int(input('Escribe el telefono: '))
                empleado = Empleado(nombre=nombre_var, apellido=apellido_var,edad=edad_var, direccion=direccion_var, telefono=telefono_var)
                empleados_insertados = EmpleadoDAO.insertar(empleado)
                log.info(f'Empleado insertado: {empleados_insertados}')
            elif opcion == 3:
                id_empleado_var = int(input('Escribe el id_empleado a modificar: '))
                nombre_var = input('Escribe el nuevo nombre: ')
                apellido_var = input('Escribe el nuevo apellido: ')
                edad_var = int(input('Escribe el edad: '))
                direccion_var = input('Escribe la direccion: ')
                telefono_var = int(input('Escribe el telefono: '))
                empleado = Empleado(id_empleado_var, nombre_var, apellido_var,edad_var, direccion_var, telefono_var)
                empleados_actualizados = EmpleadoDAO.actualizar(empleado)
                log.info(f'Empleados actualizados: {empleados_actualizados}')
            elif opcion == 4:
                id_empleado_var = int(input('Escribe el id_empleado a eliminar: '))
                empleado = Empleado(id_empleado=id_empleado_var)
                empleado_eliminado = EmpleadoDAO.eliminar(empleado)
                log.info(f'Empleado eliminado: {empleado_eliminado}')
        else:
            log.info('Saliendo de la aplicación')
    elif opcion==2:
        os.system('cls')
        opcion = None
        while opcion != 5:
            print('Opciones:')
            print('1. Listar Animal')
            print('2. Agregar Animal')
            print('3. Modificar Animal')
            print('4. Eliminar Animal')
            print('5. Salir')
            opcion = int(input('Escribe tu opcion (1-5): '))
            if opcion == 1:
                animal = AnimalDAO.seleccionar()
                for animal in animal :
                    log.info(animal)
            elif opcion == 2:
                nombre_var = input('Escribe el nombre: ')
                edad_var = int(input('Escribe el edad: '))
                grupo_pertenece_var= input('Escribir al grupo al que pertence: ')
                tipo_alimentacion_var = input('Escribe el tipo de alimentacion: ')
                habitat_var = input('Escribe el tipo de habitat : ')
                animal = Animal(nombre=nombre_var, edad=edad_var, grupo_pertenece=grupo_pertenece_var, tipo_alimentacion=tipo_alimentacion_var, habitat=habitat_var)
                animal_insertado = AnimalDAO.insertar(animal)
                log.info(f'Animal insertado: {animal_insertado}')
            elif opcion == 3:
                id_animal_var = int(input('Escribe el id_animal a modificar: '))
                nombre_var = input('Escribe el nuevo nombre: ')
                edad_var = int(input('Escribe el edad: '))
                grupo_pertenece_var= input('Escribir al grupo al que pertence: ')
                tipo_alimentacion_var = input('Escribe el tipo de alimentacion: ')
                habitat_var = input('Escribe el tipo de habitat : ')
                animal = Animal(id_animal_var, nombre_var, edad_var, grupo_pertenece_var, tipo_alimentacion_var, habitat_var)
                animal_actualizado = AnimalDAO.actualizar(animal)
                log.info(f'Empleados actualizados: {animal_actualizado}')
            elif opcion == 4:
                id_animal_var = int(input('Escribe el id_animal a eliminar: '))
                animal = Animal(id_animal=id_animal_var)
                animal_eliminado = AnimalDAO.eliminar(animal)
                log.info(f'Animal eliminado: {animal_eliminado}')
        else:
            log.info('Saliendo de la aplicación')
    elif opcion==3:
        os.system('cls')
        opcion = None
        while opcion != 5:
            print('Opciones:')
            print('1. Listar Zoologico')
            print('2. Agregar Zoologico')
            print('3. Modificar Zoologico')
            print('4. Eliminar Zoologico')
            print('5. Salir')
            opcion = int(input('Escribe tu opcion (1-5): '))
            if opcion == 1:
                zoologico = ZoologicoDAO.seleccionar()
                for zoologico in zoologico:
                    log.info(zoologico)
            elif opcion == 2:
                nombre_var = input('Escribe el nombre: ')
                direccion_var = input('Escribe el direccion: ')
                cantidad_animales_var = int(input('Escribir la cantidad de animales: '))
                cantidad_guias_var = int(input('Escribir la cantidad de guias: '))
                cantidad_cuidadores_var = int(input('Escribir la cantidad de cuidadores: '))

                zoologico = Zoologico(nombre=nombre_var, direccion=direccion_var, cantidad_animales=cantidad_animales_var, cantidad_guias=cantidad_guias_var, cantidad_cuidadores=cantidad_cuidadores_var)
                zoologico_insertado = ZoologicoDAO.insertar(zoologico)
                log.info(f'zoologico insertado: {zoologico_insertado}')
            elif opcion == 3:
                id_zoologico_var = int(input('Escribe el id_zoologico a modificar: '))
                nombre_var = input('Escribe el nombre: ')
                direccion_var = input('Escribe el direccion: ')
                cantidad_animales_var = int(input('Escribir la cantidad de animales: '))
                cantidad_guias_var = int(input('Escribir la cantidad de guias: '))
                cantidad_cuidadores_var = int(input('Escribir la cantidad de cuidadores: '))
                zoologico = Zoologico(id_zoologico_var, nombre_var, direccion_var, cantidad_animales_var, cantidad_guias_var, cantidad_cuidadores_var)
                zoologico_actualizado = ZoologicoDAO.actualizar(zoologico)
                log.info(f'zoologico actualizados: {zoologico_actualizado}')
            elif opcion == 4:
                id_zoologico_var = int(input('Escribe el id_zoologico a eliminar: '))
                zoologico = Zoologico(id_zoologico=id_zoologico_var)
                zoologico_eliminado = ZoologicoDAO.eliminar(zoologico)
                log.info(f'Animal eliminado: {zoologico_eliminado}')
        else:
            log.info('Saliendo de la aplicación')
    elif opcion==4:
        log.info('Saliendo de la aplicación')
