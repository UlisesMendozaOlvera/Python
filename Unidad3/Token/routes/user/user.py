from flask import Blueprint,request,jsonify
from sqlalchemy import exc
from models import User
from app import db,bcrypt
from auth import tokenCheck

appuser=Blueprint('appuser',__name__,template_folder='templates')


@appuser.route('/auth/registro',methods=['POST'])
def registro():
    user=request.get_json()
    userExist=User.query.filter_by(email=user['email']).first()
    if not userExist:
        usuario=User(email=user['email'],password=user['password'])
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje="Usuario creado"

        except exc.SQLAlchemyError as e:
            mensaje="error"
    else:
        mensaje="El usuario ya existe"
    return jsonify({"mensaje":mensaje})
    
@appuser.route('/auth/login',methods=['POST'])
def login():
    user=request.get_json()
    usuario=User(email=user['email'],password=user['password'])
    searchUser=User.query.filter_by(email=usuario.email).first()
    if searchUser:
        print(searchUser.password,searchUser.email)
        validation=bcrypt.check_password_hash(searchUser.password,user["password"])
        if validation:
            auth_token=usuario.encode_auth_token(user_id=searchUser.id)
            print(auth_token)
            responseObj ={
                "status":"exitoso",
                "mensaje":"login",
                "auth_token":auth_token
            }
            return jsonify(responseObj)
    return jsonify({"mensaje":"Datos Incorrectos"})

@appuser.route('/usuarios',methods=['GET'])
@tokenCheck
def getUsers(usuario):
    print(usuario)
    if usuario['admin']:
        output=[]
        usuarios=User.query.all()
        for usuario in usuarios:
            obj={}
            obj['id']=usuario.id
            obj['email']=usuario.email
            obj['password']=usuario.password
            obj['id']=usuario.registered_on
            obj['id']=usuario.admin
            output.append(obj)
        return jsonify({'usuarios':output})
            