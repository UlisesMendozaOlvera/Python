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

appempleado=Blueprint('appempleado',__name__,template_folder='templates')

@appempleado.route('/inicioAdministrador')
@login_required
def inicioAdministrador():
    empleado= Empleado.query.all()
    animal= Animal.query.all()
    zoologico= Zoologico.query.all()
    
    
    return render_template('empleado/administrador.html',empleado=empleado,animal=animal,zoologico=zoologico)  
@appempleado.route('/verEmpleado/<int:id>')
@login_required
def verEmpleado(id):
    empleado=Empleado.query.get_or_404(id)
    return render_template('empleado/detalleEmpleado.html',empleado=empleado)


@appempleado.route('/editarEmpleado/<int:id>', methods=('GET','POST'))
@login_required
def editarEmpleado(id):
    empleado=Empleado.query.get_or_404(id)
    empleado=Empleado.query.get(id)
    zoologicos=Zoologico.query.filter_by(id=empleado.id_zoolgico).first()
    puestos=Puesto.query.filter_by(id_puesto=empleado.id_puesto).first()
    
    puesto= Puesto.query.all()
    zoologico= Zoologico.query.all()

    if g.user.admin == False:
        error = f'Se requiere ser Administrador'
       
        flash(error)
        return redirect(url_for('appempleado.inicioAdministrador'))
    else:
        if request.method == 'POST':
            empleado.nombre=request.form.get('nombre')
            empleado.apellido=request.form.get('apellido')
            empleado.edad=request.form.get('edad')
            empleado.direccion=request.form.get('direccion')
            puesto=request.form.get('puestos')
            zoologico_nombre=request.form.get('zoologicos')
            puestos=Puesto.query.filter_by( nombre_puesto = puesto).first()
            zoologicos=Zoologico.query.filter_by(nombre=zoologico_nombre).first()
            empleado.id_puesto=empleado.id_puesto
            empleado.id_zoolgico=empleado.id_zoolgico
            
            
            error = None
            if not empleado.nombre:
                error = 'Se requiere un Nombre'
            
            if error is not None:
                flash(error)
            else:
                db.session.add(empleado)
                db.session.commit()
                return redirect(url_for('appempleado.inicioAdministrador'))
            
            flash(error)
            
        return render_template('empleado/editarEmpleado.html',empleado=empleado,zoologicos=zoologicos,puestos=puestos,puesto=puesto,zoologico=zoologico)

@appempleado.route('/agregaEmpleado', methods=['GET','POST'])
@login_required
def agregarEmpleado():
    zoologico= Zoologico.query.all()
    p=Puesto.query.all()
    if request.method=='POST':
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        edad=request.form.get('edad')
        direccion=request.form.get('direccion')
        puesto=request.form.get('puestos')
        zoologico_nombre=request.form.get('zoologicos')
        puestos=Puesto.query.filter_by( nombre_puesto = puesto).first()
        zoologicos=Zoologico.query.filter_by(nombre=zoologico_nombre).first()
       
        empleado=Empleado(nombre=nombre,apellido=apellido,edad=edad,direccion=direccion,id_puesto=int(puestos.id_puesto),id_zoologico=int(zoologicos.id))
        error = None
        if not nombre:
            error = 'Se requiere un nombre'
        if not direccion:
             error = 'Se requiere una dirección'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(empleado)
            db.session.commit()
            return redirect(url_for('appempleado.inicioAdministrador'))
        
        flash(error)
    return render_template('empleado/agregarEmpleado.html',zoo=zoologico,p=p)



@appempleado.route('/eliminarEmpleado/<int:id>',methods=['GET','POST'])
@login_required
def eliminarEmpleado(id):
    if g.user.admin == False:
        error = f'Se requiere ser Administrador'
       
        flash(error)
        return redirect(url_for('zoo.inicioZoologico'))
    else:
        empleado=Empleado.query.get_or_404(id)
        db.session.delete(empleado)
        db.session.commit()
        return redirect(url_for('zoo.inicioZoologico'))
    
@appempleado.route('/eliminarEmpleadoAd/<int:id>',methods=['GET','POST'])
@login_required
def eliminarEmpleadoAd(id):
    if g.user.admin == False:
        error = f'Se requiere ser Administrador'
       
        flash(error)
        return redirect(url_for('appempleado.inicioAdministrador'))
    else:
        empleado=Empleado.query.get_or_404(id)
        db.session.delete(empleado)
        db.session.commit()
        return redirect(url_for('appempleado.inicioAdministrador'))
@appempleado.route('/download/report/pdf')
def download_report_empleados():
        result = Empleado.query.all()
        zoo = Zoologico.query.all()
        puesto = Puesto.query.all()
        
        print(result)
        pdf = FPDF()
        pdf.add_page()
         
        page_width = pdf.w - 2 * pdf.l_margin
         
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Reporte de Empleados', align='C')
        pdf.ln(10)
 
        pdf.set_font('Courier', '', 12)
         
        col_width = page_width/6
         
        pdf.ln(1)
         
        th = pdf.font_size
        
        pdf.cell(10,th,str('ID'),border=1)
        pdf.cell(col_width,th,str('Nombre'),border=1)
        pdf.cell(col_width,th,str('Apellido'),border=1)
        pdf.cell(20,th,str('Edad'),border=1)
        pdf.cell(col_width,th,str('Direccion'),border=1)
        pdf.cell(col_width,th,str('Puesto'),border=1)
        pdf.cell(col_width,th,str('Zoologico'),border=1)
        
        
        pdf.ln(th)  
        for row in result:
            pdf.cell(10, th, str(row.id), border=1)
            pdf.cell(col_width, th, str(row.nombre), border=1)
            pdf.cell(col_width, th, str(row.apellido), border=1)
            pdf.cell(20, th, str(row.edad), border=1)
            pdf.cell(col_width, th, str(row.direccion), border=1)
            pdf.cell(col_width, th, str(row.id_puesto), border=1)
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
        pdf.cell(page_width, 0.0, 'Puestos', align='C')
        pdf.set_font('Courier', '', 12)
        pdf.ln(th)  
        pdf.cell(10,th,str('ID'),border=1)
        pdf.cell(180,th,str('Puesto'),border=1)
        pdf.ln(th) 
        for row in puesto:
            pdf.cell(10, th, str(row.id_puesto), border=1)
            pdf.cell(180, th, str(row.nombre_puesto), border=1)

            pdf.ln(th)
         
        pdf.ln(10)
         
        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
         
        return Response(pdf.output(dest='S'),mimetype='application/pdf',headers={'Content-Disposition':'attachment;filename=empleados_report.pdf'})
        
      
# @appempleado.route('/ver/<int:id>')
# def verDetalle(id):
#     empleado=Empleado.query.get_or_404(id)
#     return render_template('detalle.html',empleado=empleado)

# @appempleado.route('/agregar', methods=['GET','POST'])
# def agregar():
#     empleado=Empleado()
#     empleadoForm=EmpleadoForm(obj=empleado)
#     if request.method=='POST':
#         if empleadoForm.validate_on_submit():
#             empleadoForm.populate_obj(empleado)
           
#             db.session.add(empleado)
#             db.session.commit()
#             return redirect(url_for('inicio'))
#     return render_template  ('agregar.html',forma=empleadoForm)

# @appempleado.route('/editar/<int:id>',methods=['GET','POST'])
# def editar(id):
#     empleado=Empleado.query.get_or_404(id)
#     empleadoForm=EmpleadoForm(obj=empleado)
#     if request.method=='POST':
#         if empleadoForm.validate_on_submit():
#             empleadoForm.populate_obj(empleado)
            
#             db.session.add(empleado)
#             db.session.commit()
#             return redirect(url_for('inicio'))
#     return render_template  ('editar.html',forma=empleadoForm)

# @appempleado.route('/eliminar/<int:id>',methods=['GET','POST'])
# def eliminar(id):
#     empleado=Empleado.query.get_or_404(id)
#     db.session.delete(empleado)
#     db.session.commit()
#     return redirect(url_for('inicio'))