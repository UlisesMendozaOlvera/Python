from django.shortcuts import render
from gestorapp.models import Pelicula, Sucursal, Genero, Sala, TipoSala
# Create your views here.

def peliculasIndex(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculasIndex.html',{'peliculas': peliculas})

def sucursalesIndex(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursalesIndex.html',{'sucursales': sucursales})

def generosIndex(request):
    generos = Genero.objects.all()
    return render(request, 'generosIndex.html',{'generos': generos})

def salasIndex(request):
    salas = Sala.objects.all()
    return render(request, 'salasIndex.html',{'salas': salas})

def tiposSalasIndex(request):
    tiposSalas = TipoSala.objects.all()
    return render(request, 'tiposSalasIndex.html',{'tiposSalas': tiposSalas})
