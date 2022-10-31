from Persona import Persona
from Persona_dao import personaDAO
from Contrato import Contrato
from Contrato_dao import ContratoDAO
from contrato_persona import Contrato_persona
from contrato_persona_dao import contrato_personaDAO
from logger_base import log
import os

os.system('cls')
opcion = None
while opcion != 5:
     print('Opciones:')
     print('1. Listar Personas')
     print('2. Agregar Personas')
     print('3. Modificar Personas')
     print('4. Eliminar Personas')
     print('5. Consulta')

     print('6. Salir')
     opcion = int(input('Escribe tu opcion (1-6): '))
     if opcion == 1:
         personas = personaDAO.seleccionar()
         for persona in personas:
             log.info(personas)
     elif opcion == 2:
         
         nombre_var = input('Escribe el nombre: ')
         edad_var = int(input('Escribe la edad: '))
         correo_var = input('Escribe la Correo: ')
         
         No_contrato_var = int(input('Escriba el No contrato:'))
         costo_var = int(input('Escriba el costo: '))
         fecha_inicio_var=input('Ingrese la Fecha de inicio: ')
         fecha_fin_var = input('Ingrese la Fecha de fin: ')

         persona = Persona(nombre=nombre_var, edad=edad_var,
                             correo=correo_var)
         contrato =Contrato(no_contrato=No_contrato_var, costo=costo_var,fecha_inicio=fecha_inicio_var,fecha_fin=fecha_fin_var)
         personas_insertados = personaDAO.insertar(persona)
         contratos_insertados= ContratoDAO.insertar(contrato)
         contrato_persona=Contrato_persona(id_persona=persona.id,id_contrato=contrato.id)
         
         
         contrato_personas_insertados=contrato_personaDAO.insertar(contrato_persona)
         log.info(
             f' insertado: {personas_insertados} {contratos_insertados} {contrato_personas_insertados}')
     elif opcion == 3:
            id_persona_var = int(input('Escribe el id_persona a modificar: '))

            nombre_var = input('Escribe el nombre: ')
            edad_var = int(input('Escribe la edad: '))
            correo_var = input('Escribe la Correo: ')

            No_contrato_var = int(input('Escriba el No contrato:'))
            costo_var = int(input('Escriba el costo: '))
            fecha_inicio_var = input('Ingrese la Fecha de inicio: ')
            fecha_fin_var = input('Ingrese la Fecha de fin: ')
            persona = Persona(id_persona_var, nombre_var, edad_var, correo_var)
            contrato = Contrato(id_persona_var, No_contrato_var, costo_var, fecha_inicio_var, fecha_fin_var)
            personas_insertados = personaDAO.actualizar(persona)
            contratos_insertados = ContratoDAO.actualizar(contrato)                        
            
            log.info(
                 f' insertado: {personas_insertados} {contratos_insertados} ')
     elif opcion == 4:
         id_persona_var = int(
             input('Escribe el id_persona a eliminar: '))
         persona = Persona(id=id_persona_var)
         contrato=Contrato(id=id_persona_var)
         persona_eliminado = personaDAO.eliminar(persona)
         contrato_eliminado = ContratoDAO.eliminar(contrato)

         log.info(f'eliminado: {persona_eliminado} {contrato_eliminado}')
     else:
           log.info('Saliendo de la aplicación')
