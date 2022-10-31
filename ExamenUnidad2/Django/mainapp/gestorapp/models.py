from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    def _str_(self):
        return f'{self.id} {self.nombre} {self.direccion}'

class TipoSala(models.Model):
    descripcion = models.CharField(max_length = 255)
    num_butacas = models.CharField(max_length = 255)
    def _str_(self):
        return f'{self.id} {self.descripcion} {self.num_butacas}'

class Genero(models.Model):
    descripcion = models.CharField(max_length = 255)
    def _str_(self):
        return f'{self.id} {self.descripcion}'

class Sala(models.Model):
    numero = models.CharField(max_length=255)    
    sucursal = models.ForeignKey(Sucursal, on_delete = models.CASCADE)
    tipo_sala = models.ForeignKey(TipoSala, on_delete= models.CASCADE)
    def _str_(self):
        return f'{self.id} {self.numero}'

class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    sinopsis = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete= models.CASCADE)
    sala = models.ForeignKey(Sala, null=True, on_delete = models.CASCADE)
    def _str_(self):
        return f'{self.id} {self.nombre} {self.sinopsis}'
    

    
