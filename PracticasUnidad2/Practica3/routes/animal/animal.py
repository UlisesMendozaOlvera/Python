from flask import Blueprint,request,jsonify,render_template,redirect,session,url_for,g,flash,Response
from sqlalchemy import exc
from models import Empleado
from app import db,bcrypt
from auth import tokenCheck
from models import Animal, Empleado, Zoologico,Puesto
from forms import EmpleadoForm,AnimalForm,ZoologicoForm
from routes.imagen.imagen import render_image
from routes.user.user import login_required
from fpdf import FPDF

animal=Blueprint('animal',__name__,template_folder='templates')




@animal.route('/editarAnimal/<int:id>', methods=('GET','POST'))
@login_required
def editarAnimal(id):
    animal=Animal.query.get_or_404(id)
    animal=Animal.query.get(id)
    zoologico= Zoologico.query.all()
    cuidador= Empleado.query.all()
    
    if g.user.admin == False:
        error = f'Se requiere ser Administrador'
       
        flash(error)
        return redirect(url_for('zoo.inicioZoologico'))
    else:
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            edad = request.form.get('edad')
            grupo_pertenece = request.form.get('grupo_pertenece')
            tipo_alimentacion = request.form.get('tipo_alimentacion')
            habitat = request.form.get('habitat')
            cuidador_id = request.form.get('cuidador')
            id_zoolgico = request.form.get('zoologicos')
           
            cuidador_nombre=Empleado.query.filter_by( nombre =cuidador_id ).first()
            zoologicos=Zoologico.query.filter_by(nombre=id_zoolgico).first()
            animal=Animal(nombre=nombre,edad=edad,grupo_pertenece=grupo_pertenece,tipo_alimentacion=tipo_alimentacion,habitat=habitat,cuidador_id=int(cuidador_nombre.id),id_zoolgico=int(zoologicos.id))
            error = None
            if not nombre:
                error = 'Se requiere un Nombre'
            
            if error is not None:
                flash(error)
            else:
                db.session.add(animal)
                db.session.commit()
                return redirect(url_for('zoo.inicioZoologico'))
            
            flash(error)
            
        return render_template('animal/editarAnimal.html',emp=cuidador,zoo=zoologico,animal=animal)

@animal.route('/agregarAnimal', methods=['GET','POST'])
@login_required
def agregarAnimal():
    zoologico= Zoologico.query.all()
    cuidador= Empleado.query.all()
    
    
    if request.method=='POST':
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        grupo_pertenece = request.form.get('grupo_pertenece')
        tipo_alimentacion = request.form.get('tipo_alimentacion')
        habitat = request.form.get('habitat')
        cuidador_id = request.form.get('cuidador')
        id_zoolgico = request.form.get('zoologicos')
        
        cuidador_nombre=Empleado.query.filter_by( nombre =cuidador_id ).first()
        zoologicos=Zoologico.query.filter_by(nombre=id_zoolgico).first()
        animal=Animal(nombre=nombre,edad=edad,grupo_pertenece=grupo_pertenece,tipo_alimentacion=tipo_alimentacion,habitat=habitat,cuidador_id=int(cuidador_nombre.id),id_zoolgico=int(zoologicos.id))
        
        error = None
        if not nombre:
            error = 'Se requiere un nombre'
        if not edad:
             error = 'Se requiere una edad'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(animal)
            db.session.commit()
            return redirect(url_for('zoo.inicioZoologico'))
        
        flash(error)
    return render_template('animal/agregarAnimal.html',zoo=zoologico,emp=cuidador)



@animal.route('/eliminarAnimal/<int:id>',methods=['GET','POST'])
@login_required
def eliminarAnimal(id):
    if g.user.admin == False:
        error = f'Se requiere ser Administrador'
       
        flash(error)
        return redirect(url_for('zoo.inicioZoologico'))
    else:
        animal=Animal.query.get_or_404(id)
        db.session.delete(animal)
        db.session.commit()
        return redirect(url_for('zoo.inicioZoologico'))
    
@animal.route('/download/report-animales/pdf')
def download_report_animales():
        result = Animal.query.all()
        zoo = Zoologico.query.all()
        puesto = Empleado.query.all()
        
        print(result)
        pdf = FPDF()
        pdf.add_page()
         
        page_width = pdf.w - 2 * pdf.l_margin
         
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Reporte de Animales', align='C')
        pdf.ln(10)
 
        pdf.set_font('Courier', '', 12)
         
        col_width = page_width/6
         
        pdf.ln(1)
         
        th = pdf.font_size
        
        pdf.cell(10,th,str('ID'),border=1)
        pdf.cell(20,th,str('Nombre'),border=1)
        pdf.cell(15,th,str('Edad'),border=1)
        pdf.cell(25,th,str('Grupo'),border=1)
        pdf.cell(col_width,th,str('Alimentacion'),border=1)
        pdf.cell(col_width,th,str('Habitat'),border=1)
        pdf.cell(col_width,th,str('Cuidador'),border=1)
        pdf.cell(col_width,th,str('Zoologico'),border=1)
        
        
        
        pdf.ln(th)  
        for row in result:
            pdf.cell(10, th, str(row.id), border=1)
            pdf.cell(20, th, str(row.nombre), border=1)
            pdf.cell(15, th, str(row.edad), border=1)
            pdf.cell(25, th, str(row.grupo_pertenece), border=1)
            pdf.cell(col_width, th, str(row.tipo_alimentacion), border=1)
            pdf.cell(col_width, th, str(row.habitat), border=1)
            pdf.cell(col_width, th, str(row.cuidador_id), border=1)
            pdf.cell(col_width, th, str(row.id_zoolgico), border=1)
            pdf.ln(th)
       
        pdf.ln(th)  
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Zoológicos', align='C')
        pdf.set_font('Courier', '', 12)
        pdf.ln(th)
        pdf.ln(1)
        pdf.cell(10,th,str('ID'),border=1)
        pdf.cell(180,th,str('Nombre'),border=1)
        pdf.ln(th)  
        for row in zoo:
            pdf.cell(10, th, str(row.id), border=1)
            pdf.cell(70, th, str(row.nombre), border=1)
            pdf.multi_cell(110, th, str(row.direccion), border=1)
            
            pdf.ln(th)
        
        
        pdf.ln(th)  
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Empleados', align='C')
        pdf.set_font('Courier', '', 12)
        pdf.ln(th)  
        pdf.cell(10,th,str('ID'),border=1)
        pdf.cell(180,th,str('Nombre'),border=1)
        pdf.ln(th) 
        for row in puesto:
            pdf.cell(10, th, str(row.id), border=1)
            pdf.cell(180, th, str(row.nombre), border=1)

            pdf.ln(th)
         
        pdf.ln(10)
         
        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
         
        return Response(pdf.output(dest='S'),mimetype='application/pdf',headers={'Content-Disposition':'attachment;filename=animales_report.pdf'})
        