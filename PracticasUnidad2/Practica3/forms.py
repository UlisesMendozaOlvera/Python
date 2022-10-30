from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class EmpleadoForm(FlaskForm):
    nombre= StringField('Nombre',validators=[DataRequired()])
    apellido= StringField('Apellido')
    edad= IntegerField('Edad',validators=[DataRequired()])
    direccion= StringField('Direccion')
    
    enviar=SubmitField('Enviar')

class AnimalForm(FlaskForm):
    nombre= StringField('Nombre',validators=[DataRequired()])
    edad= IntegerField('Edad')
    grupo_pertenece= StringField('Grupo al que pertenece')
    tipo_alimentacion= StringField('Tipo de alimentacion')
    habitat= StringField('Habitat')
    enviar=SubmitField('Enviar')

class ZoologicoForm(FlaskForm):
    nombre= StringField('Nombre',validators=[DataRequired()])
    direccion= StringField('Direccion')
    cantidad_animales= IntegerField('Cantidad de animales')
    cantidad_guias= IntegerField('Cantidad de guias')
    cantidad_cuidadores= IntegerField('Cantidad de cuidadores')
    enviar=SubmitField('Enviar')