from flask import Blueprint,request,jsonify,render_template,redirect,session,url_for,g,flash
from sqlalchemy import exc
from models import Zoologico,Animal
from models import User

from app import db,bcrypt
from auth import tokenCheck
from config import BaseConfig
import functools
from os import abort, error
from routes.imagen.imagen import render_image

from routes.user.user import login_required

zoo=Blueprint('zoo',__name__,template_folder='templates', url_prefix='/zoo')

@zoo.route('/inicioZoologico')
@login_required
def inicioZoologico():
    zoologico= Zoologico.query.all()
    animal= Animal.query.all()
    
    user=User
    return render_template('zoologico/inicio_zoologico.html',zoologico=zoologico,animal=animal)

@zoo.route('/verZoologico/<int:id>')
@login_required
def verZoologico(id):
    zoologico=Zoologico.query.get_or_404(id)
    return render_template('zoologico/detalleZoologico.html',zoologico=zoologico)


@zoo.route('/editarZoologico/<int:id>', methods=('GET','POST'))
@login_required
def editarZoologico(id):
    zoologico=Zoologico.query.get_or_404(id)
    zoologico=Zoologico.query.get(id)
    if g.user.admin == False:
        error = f'Se requiere ser Administrador'
       
        flash(error)
        return redirect(url_for('zoo.inicioZoologico'))
    else:
        if request.method == 'POST':
            zoologico.nombre = request.form.get('nombre')
            zoologico.direccion = request.form.get('direccion')

            error = None
            if not zoologico.nombre:
                error = 'Se requiere un Nombre'
            
            if error is not None:
                flash(error)
            else:
                db.session.add(zoologico)
                db.session.commit()
                return redirect(url_for('zoo.inicioZoologico'))
            
            flash(error)
            
        return render_template('zoologico/editarZoologico.html',zoologico=zoologico)

@zoo.route('/agregaZoologico', methods=['GET','POST'])
@login_required
def agregarZoologico():
   
    if request.method=='POST':
        nombre=request.form.get('nombre')
        direccion=request.form.get('direccion')
        file = request.files['file']
        data = file.read()
        render_file = render_image(data)
        zoologico=Zoologico(nombre=nombre,direccion=direccion,data=data,rendered_data=render_file)
        error = None
        if not nombre:
            error = 'Se requiere un nombre'
        if not direccion:
             error = 'Se requiere una dirección'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(zoologico)
            db.session.commit()
            return redirect(url_for('zoo.inicioZoologico'))
        
        flash(error)
    return render_template('zoologico/agregarZoologico.html')



@zoo.route('/eliminarZoologico/<int:id>',methods=['GET','POST'])
@login_required
def eliminarZoologico(id):
    if g.user.admin == False:
        error = f'Se requiere ser Administrador'
       
        flash(error)
        return redirect(url_for('zoo.inicioZoologico'))
    else:
        zoologico=Zoologico.query.get_or_404(id)
        db.session.delete(zoologico)
        db.session.commit()
        return redirect(url_for('zoo.inicioZoologico'))