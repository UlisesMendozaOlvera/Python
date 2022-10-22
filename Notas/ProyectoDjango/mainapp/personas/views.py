
from tracemalloc import get_object_traceback
from django.shortcuts import render, get_object_or_404,redirect
from personas.models import Persona
from personas.form import PersonaForm

# Create your views here.
def detallePersona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request,'detalle.html',{'persona':persona})

def nuevaPersona(request):
    if request.method=="POST":
        formaPersona=PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
            formaPersona=PersonaForm()
            return render(request,'agregar.html',{'formaPersona':formaPersona})
    
def editarPersona(request,id):
    persona=get_object_or_404(Persona,pk=id)
    if request.method=='POST':
        formaPersona=PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona=PersonaForm(instance=persona)
        return render(request,'editar.html',{'formaPersona':formaPersona})
# end def

def eliminarPersona(request,id):
    persona=get_object_or_404(Persona,pk=id)
    if persona:
        persona.delete()
    return redirect('index')    
# end def