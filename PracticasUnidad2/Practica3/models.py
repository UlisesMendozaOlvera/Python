import jwt
import datetime
from config import BaseConfig
from app import db,bcrypt

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)
    registered_on=db.Column(db.DateTime,nullable=False)
    admin=db.Column(db.Boolean,nullable=False,default=True)
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data to render the pic in browser

    def __init__(self,email,password,admin=False,data=0,rendered_data="")->None:
        self.email=email
        self.password=bcrypt.generate_password_hash(password,BaseConfig.BCRYPT_LOG_ROUNDS).decode()
        self.registered_on=datetime.datetime.now()
        self.admin=admin
        self.data=data
        self.rendered_data=rendered_data
        
    
    def encode_auth_token(self, user_id):
        try:
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(days=0,minutes=50),
                'iat':datetime.datetime.utcnow(),
                'sub':user_id

            }
            print(payload)
            return jwt.encode(payload,BaseConfig.SECRET_KEY,algorithm='HS256')
        except Exception as e:
            return e
   
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload=jwt.decode(auth_token,BaseConfig.SECRET_KEY,algorithm=['HS256'])
            
            return payload['sub']
        except jwt.ExpiredSignatureError as e:
            return "Token expirado"
        except jwt.InvalidTokenError as e:
            return "Token no valido"
        
class Zoologico(db.Model):
    __tablename__="zoologico"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre =db.Column(db.String(250),nullable=False)
    direccion=db.Column(db.String(250),nullable=False)
    data = db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download
    rendered_data = db.Column(db.Text, nullable=False)#Data t
    def __init__(self,nombre,direccion,data=0,rendered_data="")->None:
        self.nombre=nombre
        self.direccion=direccion
        self.data=data
        self.rendered_data=rendered_data
        
    
class Puesto(db.Model):
    __tablename__="puesto"
    id_puesto=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_puesto=db.Column(db.String(250),nullable=False)
    
    def __init__(self,nombre_puesto) -> None:
        self.nombre_puesto=nombre_puesto

class Empleado(db.Model):
    __tablename__="empleado"
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre =db.Column(db.String(250),nullable=False)
    apellido=db.Column(db.String(250),nullable=False)
    edad=db.Column(db.String(30))
    direccion=db.Column(db.String(250),nullable=False)
    id_puesto=db.Column(db.Integer,db.ForeignKey('puesto.id_puesto'))
   
    id_zoolgico=db.Column(db.Integer,db.ForeignKey('zoologico.id'))
    

    def __init__(self,nombre,apellido,edad,direccion,id_puesto,id_zoologico)->None:
            self.nombre=nombre
            self.apellido=apellido
            self.edad=edad
            self.direccion=direccion
            self.id_puesto=id_puesto
            self.id_zoolgico=id_zoologico
        
 
class Animal(db.Model):
    __tablename__="animal"
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre =db.Column(db.String(250),nullable=False)
    edad=db.Column(db.String(30))
    grupo_pertenece=db.Column(db.String(250),nullable=False)
    tipo_alimentacion=db.Column(db.String(250),nullable=False)
    habitat=db.Column(db.String(250),nullable=False)
    cuidador_id=db.Column(db.Integer,db.ForeignKey('empleado.id'))
   
    id_zoolgico=db.Column(db.Integer,db.ForeignKey('zoologico.id'))
  
    
    def __init__(self,nombre,edad,grupo_pertenece,tipo_alimentacion,habitat,cuidador_id,id_zoolgico) -> None:
        self.nombre=nombre
        self.edad=edad
        self.grupo_pertenece=grupo_pertenece
        self.tipo_alimentacion=tipo_alimentacion
        self.habitat=habitat
        self.cuidador_id=cuidador_id
        self.id_zoolgico=id_zoolgico


   

