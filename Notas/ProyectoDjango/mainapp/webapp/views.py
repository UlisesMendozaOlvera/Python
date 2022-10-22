from django.shortcuts import render
from personas.models import Persona
# Create your views here.
def bienvenido(request):
    personas=Persona.objects.order_by('id')
    return render(request,'hola.html',{'personas':personas})