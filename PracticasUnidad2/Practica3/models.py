from app import db
class Empleado(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(250))
    apellido=db.Column(db.String(250))
    edad=db.Column(db.Integer)
    direccion=db.Column(db.String(250))
 

    def __str__(self) -> str:
        return (
            f'ID: {self.id},'
            f'Nombre: {self.nombre},'
            f'Apellido: {self.apellido},'
            f'Edad: {self.edad},'
            f'Direccion: {self.direccion}'
            

        )        
    # end def
class Animal(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(250))
    edad=db.Column(db.Integer)
    grupo_pertenece=db.Column(db.String(250))
    tipo_alimentacion=db.Column(db.String(250))
    habitat=db.Column(db.String(250))

    def __str__(self) -> str:
        return (
            f'ID: {self.id},'
            f'Nombre: {self.nombre},'
            f'Edad: {self.edad},'
            f'Grupo al que Pertenece: {self.grupo_pertenece},'
            f'Tipo de Alimentacion: {self.tipo_alimentacion},'
            f'Grupo al que Pertenece: {self.habitat}'
        )  
        
class Zoologico(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(250))
    direccion=db.Column(db.String(250))
    cantidad_animales=db.Column(db.Integer)
    cantidad_guias=db.Column(db.Integer)
    cantidad_cuidadores=db.Column(db.Integer)

    def __str__(self) -> str:
        return (
            f'ID: {self.id},'
            f'Nombre: {self.nombre},'
            f'Direccion: {self.direccion},'
            f'Grupo al que Pertenece: {self.cantidad_animales},'
            f'Tipo de Alimentacion: {self.cantidad_guias},'
            f'Grupo al que Pertenece: {self.cantidad_cuidadores}'
        )  