import logging
from flask import Flask,request,url_for,render_template,redirect
from database import db 
from flask_migrate import Migrate
from models import Animal, Empleado, Zoologico
from forms import EmpleadoForm,AnimalForm,ZoologicoForm

app= Flask(__name__)

USER_DB='postgres'
PASS_DB='bumo'
URL_DB='localhost'
NAME_DB='practica3'
FULL_URL_DB= f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI']= FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)

migrate=Migrate()
migrate.init_app(app,db) 
#flask db stamp head
#flask db init 
#flask db migrate
#flask db upgrade
app.config["SECRET_KEY"]="una llave muy secreta"
logging.basicConfig(filename="error.log",level=logging.DEBUG)
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def verObjetos():
   
    return render_template('index.html')
    
# end def
@app.route('/empleado.html')
def inicio():
    empleados= Empleado.query.all()
    return render_template('empleado.html',empleados=empleados)    
@app.route('/ver/<int:id>')
def verDetalle(id):
    empleado=Empleado.query.get_or_404(id)
    return render_template('detalle.html',empleado=empleado)

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    empleado=Empleado()
    empleadoForm=EmpleadoForm(obj=empleado)
    if request.method=='POST':
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            app.logger.debug(f'Empleado a insertar: {empleado}')
            db.session.add(empleado)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template  ('agregar.html',forma=empleadoForm)

@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    empleado=Empleado.query.get_or_404(id)
    empleadoForm=EmpleadoForm(obj=empleado)
    if request.method=='POST':
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            app.logger.debug(f'Empleado a Actualizado: {empleado}')
            db.session.add(empleado)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template  ('editar.html',forma=empleadoForm)

@app.route('/eliminar/<int:id>',methods=['GET','POST'])
def eliminar(id):
    empleado=Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('inicio'))
#Clase Animal
@app.route('/animal.html')
def inicioAnimal():
    animales= Animal.query.all()
    return render_template('Animal.html',animales=animales)    

@app.route('/verAnimal/<int:id>')
def verAnimal(id):
    animal=Animal.query.get_or_404(id)
    return render_template('detalleAnimal.html',animal=animal)

@app.route('/agregaAnimal', methods=['GET','POST'])
def agregarAnimal():
    animal=Animal()
    animalForm=AnimalForm(obj=animal)
    if request.method=='POST':
        if animalForm.validate_on_submit():
            animalForm.populate_obj(animal)
            app.logger.debug(f'Animal a insertar: {animal}')
            db.session.add(animal)
            db.session.commit()
            return redirect(url_for('inicioAnimal'))
    return render_template('agregarAnimal.html',forma=animalForm)

@app.route('/editarAnimal/<int:id>',methods=['GET','POST'])
def editarAnimal(id):
    animal=Animal.query.get_or_404(id)
    animalForm=AnimalForm(obj=animal)
    if request.method=='POST':
        if animalForm.validate_on_submit():
            animalForm.populate_obj(animal)
            app.logger.debug(f'Animal a Actualizado: {animal}')
            db.session.add(animal)
            db.session.commit()
            return redirect(url_for('inicioAnimal'))
    return render_template('editarAnimal.html',forma=animalForm)

@app.route('/eliminarAnimal/<int:id>',methods=['GET','POST'])
def eliminarAnimal(id):
    animal=Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    return redirect(url_for('inicioAnimal'))

#Clase Zoologico
@app.route('/zoologico.html')
def inicioZoologico():
    zoologico= Zoologico.query.all()
    return render_template('zoologico.html',zoologico=zoologico)    

@app.route('/verZoologico/<int:id>')
def verZoologico(id):
    zoologico=Zoologico.query.get_or_404(id)
    return render_template('detalleZoologico.html',zoologico=zoologico)

@app.route('/agregaZoologico', methods=['GET','POST'])
def agregarZoologico():
    zoologico=Zoologico()
    zoologicoForm=ZoologicoForm(obj=zoologico)
    if request.method=='POST':
        if zoologicoForm.validate_on_submit():
            zoologicoForm.populate_obj(zoologico)
            app.logger.debug(f'Zoologico a insertar: {zoologico}')
            db.session.add(zoologico)
            db.session.commit()
            return redirect(url_for('inicioZoologico'))
    return render_template('agregarZoologico.html',forma=zoologicoForm)

@app.route('/editarZoologico/<int:id>',methods=['GET','POST'])
def editarZoologico(id):
    zoologico=Zoologico.query.get_or_404(id)
    zoologicoForm=ZoologicoForm(obj=zoologico)
    if request.method=='POST':
        if zoologicoForm.validate_on_submit():
            zoologicoForm.populate_obj(zoologico)
            app.logger.debug(f'Zoologico a Actualizado: {zoologico}')
            db.session.add(zoologico)
            db.session.commit()
            return redirect(url_for('inicioZoologico'))
    return render_template('editarZoologico.html',forma=zoologicoForm)

@app.route('/eliminarZoologico/<int:id>',methods=['GET','POST'])
def eliminarZoologico(id):
    zoologico=Zoologico.query.get_or_404(id)
    db.session.delete(zoologico)
    db.session.commit()
    return redirect(url_for('inicioZoologico'))