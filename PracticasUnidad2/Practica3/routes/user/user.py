import base64
from flask import Blueprint,request,jsonify,render_template,redirect,session,url_for,g,flash
from sqlalchemy import exc
from models import User
from app import db,bcrypt
from auth import tokenCheck
from config import BaseConfig
import functools
from os import error

from app import db
from routes.imagen.imagen import render_image


auth=Blueprint('auth',__name__,template_folder='templates', url_prefix='/auth')


#Registrar un usuario 
@auth.route('/register',methods=('GET','POST') )
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
       
        file = request.files['file']
        data = file.read()
        render_file = render_image(data)
       
       
        user = User(email=username,password=password,data=data,rendered_data=render_file)
       
        print(user.data)
        error = None
        if not username:
            error = 'Se requiere nombre de usuario'
        elif not password:
            error = 'Se requiere contraseña'
        
        user_name = User.query.filter_by(email = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya esta registrado'
        flash(error)
        
    return render_template('auth/registrar.html')


#Iniciar Sesión
@auth.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = None
        usuario=User(email=username,password=password)
        user = User.query.filter_by(email = usuario.email).first()
        validation=bcrypt.check_password_hash(user.password, password)
        image = user.rendered_data
        #print(user.email,user.password,usuario.password,validation)
        if user == None:
            error = 'Nombre de usuario incorrecto'
        elif not validation:
            error = 'Contraseña incorrecta'
            
        if error is None:
            if validation:
                auth_token=usuario.encode_auth_token(user_id=user.id)
                print(auth_token)
                
                session.clear()
            
                session['user_id'] = user.id
            if user.admin == True:
               
                return redirect(url_for('appempleado.inicioAdministrador'))
            else:
                return redirect(url_for('zoo.inicioZoologico'))
        
        flash(error)
        
    return render_template('auth/login.html')


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
# @auth.route('/auth/registro',methods=['POST'])
# def registro():
#     user=request.get_json()
#     userExist=User.query.filter_by(email=user['email']).first()
#     if not userExist:
#         usuario=User(email=user['email'],password=user['password'])
#         try:
#             db.session.add(usuario)
#             db.session.commit()
#             mensaje="Usuario creado"

#         except exc.SQLAlchemyError as e:
#             mensaje="error"
#     else:
#         mensaje="El usuario ya existe"
#     return jsonify({"mensaje":mensaje})
    
# @auth.route('/auth/login',methods=['POST'])
# def login():
#     user=request.get_json()
#     usuario=User(email=user['email'],password=user['password'])
#     searchUser=User.query.filter_by(email=usuario.email).first()
#     if searchUser:
#         print(searchUser.password,searchUser.email)
#         validation=bcrypt.check_password_hash(searchUser.password,user["password"])
#         if validation:
#             auth_token=usuario.encode_auth_token(user_id=searchUser.id)
#             print(auth_token)
#             responseObj ={
#                 "status":"exitoso",
#                 "mensaje":"login",
#                 "auth_token":auth_token
#             }
#             return jsonify(responseObj)
#     return jsonify({"mensaje":"Datos Incorrectos"})

# @auth.route('/usuarios',methods=['GET'])
# @tokenCheck
# def getUsers(usuario):
#     print(usuario)
#     if usuario['admin']:
#         output=[]
#         usuarios=User.query.all()
#         for usuario in usuarios:
#             obj={}
#             obj['id']=usuario.id
#             obj['email']=usuario.email
#             obj['password']=usuario.password
#             obj['id']=usuario.registered_on
#             obj['id']=usuario.admin
#             output.append(obj)
#         return jsonify({'usuarios':output})
            