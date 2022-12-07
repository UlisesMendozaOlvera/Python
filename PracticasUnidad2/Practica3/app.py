from flask import Flask,request,jsonify,redirect,url_for,render_template,Response
from flask_cors import CORS
from database import db 
from encript import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from models import Empleado, User
from sqlalchemy import exc
from functools import wraps
from routes.user.user import auth
from routes.zoologico.zoologico import zoo
from routes.empleado.empleado import appempleado
from routes.animal.animal import animal






#from routes.images.images import imageUser

app=Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



app.register_blueprint(auth)
app.register_blueprint(zoo)
app.register_blueprint(appempleado)
app.register_blueprint(animal)




#app.register_blueprint(imageUser)

app.config.from_object(BaseConfig)
CORS(app)
db.init_app(app)
migrate=Migrate()
migrate.init_app(app,db)
#flask db stamp head
#flask db init 
#flask db migrate
#flask db upgrade

# logging.basicConfig(filename="error.log",level=logging.DEBUG)
# @app.route('/')
# @app.route('/index')
# @app.route('/index.html')
# def verObjetos():
   
#     return render_template('index.html')
    
# # end def

# #Clase Animal
# @app.route('/animal.html')
# def inicioAnimal():
#     animales= Animal.query.all()
#     return render_template('Animal.html',animales=animales)    

# @app.route('/verAnimal/<int:id>')
# def verAnimal(id):
#     animal=Animal.query.get_or_404(id)
#     return render_template('detalleAnimal.html',animal=animal)

# @app.route('/agregaAnimal', methods=['GET','POST'])
# def agregarAnimal():
#     animal=Animal()
#     animalForm=AnimalForm(obj=animal)
#     if request.method=='POST':
#         if animalForm.validate_on_submit():
#             animalForm.populate_obj(animal)
#             app.logger.debug(f'Animal a insertar: {animal}')
#             db.session.add(animal)
#             db.session.commit()
#             return redirect(url_for('inicioAnimal'))
#     return render_template('agregarAnimal.html',forma=animalForm)

# @app.route('/editarAnimal/<int:id>',methods=['GET','POST'])
# def editarAnimal(id):
#     animal=Animal.query.get_or_404(id)
#     animalForm=AnimalForm(obj=animal)
#     if request.method=='POST':
#         if animalForm.validate_on_submit():
#             animalForm.populate_obj(animal)
#             app.logger.debug(f'Animal a Actualizado: {animal}')
#             db.session.add(animal)
#             db.session.commit()
#             return redirect(url_for('inicioAnimal'))
#     return render_template('editarAnimal.html',forma=animalForm)

# @app.route('/eliminarAnimal/<int:id>',methods=['GET','POST'])
# def eliminarAnimal(id):
#     animal=Animal.query.get_or_404(id)
#     db.session.delete(animal)
#     db.session.commit()
#     return redirect(url_for('inicioAnimal'))

# #Clase Zoologico
# @app.route('/zoologico.html')
# def inicioZoologico():
#     zoologico= Zoologico.query.all()
#     return render_template('zoologico.html',zoologico=zoologico)    

# @app.route('/verZoologico/<int:id>')
# def verZoologico(id):
#     zoologico=Zoologico.query.get_or_404(id)
#     return render_template('detalleZoologico.html',zoologico=zoologico)

# @app.route('/agregaZoologico', methods=['GET','POST'])
# def agregarZoologico():
#     zoologico=Zoologico()
#     zoologicoForm=ZoologicoForm(obj=zoologico)
#     if request.method=='POST':
#         if zoologicoForm.validate_on_submit():
#             zoologicoForm.populate_obj(zoologico)
#             app.logger.debug(f'Zoologico a insertar: {zoologico}')
#             db.session.add(zoologico)
#             db.session.commit()
#             return redirect(url_for('inicioZoologico'))
#     return render_template('agregarZoologico.html',forma=zoologicoForm)

# @app.route('/editarZoologico/<int:id>',methods=['GET','POST'])
# def editarZoologico(id):
#     zoologico=Zoologico.query.get_or_404(id)
#     zoologicoForm=ZoologicoForm(obj=zoologico)
#     if request.method=='POST':
#         if zoologicoForm.validate_on_submit():
#             zoologicoForm.populate_obj(zoologico)
#             app.logger.debug(f'Zoologico a Actualizado: {zoologico}')
#             db.session.add(zoologico)
#             db.session.commit()
#             return redirect(url_for('inicioZoologico'))
#     return render_template('editarZoologico.html',forma=zoologicoForm)

# @app.route('/eliminarZoologico/<int:id>',methods=['GET','POST'])
# def eliminarZoologico(id):
#     zoologico=Zoologico.query.get_or_404(id)
#     db.session.delete(zoologico)
#     db.session.commit()
#     return redirect(url_for('inicioZoologico'))