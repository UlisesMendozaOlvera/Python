from flask import Blueprint,request,jsonify,Flask,request,url_for,render_template,redirect
from sqlalchemy import exc
from models import Empleado
from app import db,bcrypt,app
#from auth import tokenCheck
from models import Animal, Empleado, Zoologico
from forms import EmpleadoForm,AnimalForm,ZoologicoForm

appempleado=Blueprint('appempleado',__name__,template_folder='templates')

@appempleado.route('/empleado')
def inicio():
    empleados= Empleado.query.all()
    return render_template('empleado.html',empleados=empleados)    
@appempleado.route('/ver/<int:id>')
def verDetalle(id):
    empleado=Empleado.query.get_or_404(id)
    return render_template('detalle.html',empleado=empleado)

@appempleado.route('/agregar', methods=['GET','POST'])
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

@appempleado.route('/editar/<int:id>',methods=['GET','POST'])
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

@appempleado.route('/eliminar/<int:id>',methods=['GET','POST'])
def eliminar(id):
    empleado=Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('inicio'))