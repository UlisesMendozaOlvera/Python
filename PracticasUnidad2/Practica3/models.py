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

    def __init__(self,email,password,admin=False)->None:
        self.email=email
        self.password=bcrypt.generate_password_hash(password,BaseConfig.BCRYPT_LOG_ROUNDS).decode()
        self.registered_on=datetime.datetime.now()
        self.admin=admin
    
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

class Puesto(db.Model):
    __tablename__="puesto"
    id_puesto=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_puesto=db.Column(db.String(250),nullable=False)

class Empleado(db.Model):
    __tablename__="empleado"
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre =db.Column(db.String(250),nullable=False)
    apellido=db.Column(db.String(250),nullable=False)
    edad=db.Column(db.Integer)
    direccion=db.Column(db.String(250),nullable=False)
    id_puesto=db.Column(db.Integer,db.ForeignKey('puesto.id_puesto'))
    nombre_puesto=db.relationship('Puesto',backref='puesto')
    id_zoolgico=db.Column(db.Integer,db.ForeignKey('zoologico.id'))
    nombre_zoologico=db.relationship('Zoologico',backref='zoologico')
   
 
    # end def
class Animal(db.Model):
    __tablename__="animal"
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre =db.Column(db.String(250),nullable=False)
    edad=db.Column(db.Integer)
    grupo_pertenece=db.Column(db.String(250),nullable=False)
    tipo_alimentacion=db.Column(db.String(250),nullable=False)
    habitat=db.Column(db.String(250),nullable=False)
    cuidador_id=db.Column(db.Integer,db.ForeignKey('empleado.id'))
    cuidador_nombre=db.relationship('Empleado',backref='empleado')
    id_zoolgico=db.Column(db.Integer,db.ForeignKey('zoologico.id'))
    nombre_zoologico=db.relationship('Zoologico',backref='zoologico')
    


   

