from django.db import models

# Create your models here.

class Transportista(models.Model):
    rfc= models.CharField(max_length=255)
    nombre= models.CharField(max_length=255)
    apellido= models.CharField(max_length=255)
    direccion= models.CharField(max_length=255)
    
    def __str__(self):
        return f'Transportista {self.id}: {self.rfc} {self.nombre} {self.apellido} {self.direccion}'
    

class Automoviles(models.Model):
    color= models.CharField(max_length=255)
    placas= models.CharField(max_length=255)
    marca= models.CharField(max_length=255)
    linea= models.CharField(max_length=255)
    modelo= models.CharField(max_length=255)
    estatus= models.CharField(max_length=255)
    transportista = models.ForeignKey(Transportista,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'Automoviles {self.id}: {self.color} {self.placas} {self.marca} {self.linea} {self.modelo} {self.estatus}'

class EquipoGPS(models.Model):
    celular= models.IntegerField()
    sim= models.IntegerField()
    fabricante= models.CharField(max_length=255)
    modelo= models.CharField(max_length=255)
    estatus= models.CharField(max_length=255)
    transportista = models.ForeignKey(Transportista,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'Automoviles {self.id}: {self.celular} {self.sim} {self.fabricante} {self.modelo} {self.estatus}'
    
class AutomovilesEquipos(models.Model):
    fechaAsignacion= models.DateField()
    fechaDesasignacion= models.DateField()
    transportista = models.ForeignKey(Transportista,on_delete=models.SET_NULL,null=True)
    automoviles = models.ForeignKey(Automoviles,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'Automoviles {self.id}: {self.fechaAsignacion} {self.fechaDesasignacion}'