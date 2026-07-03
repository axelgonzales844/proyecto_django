from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto


def registros(request):
      alumnos=Alumnos.objects.all()

      return render(request,"registros/principal.html",{'alumnos':alumnos
                                                        })
#indicamos el lugar donde se renderiza el resultado de esta vista y enviamos la list de alumnos recuperados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()
            return render(request,'registros/consultarComentario.html',
                          {'comentarios':comentarios})
            return render(request,'registros/contacto.html')
        form = ComentarioContactoForm()
        return render(request,'registro/contacto.html',{'form':form})
    
def contacto(request):
    return render(request,"registros/contacto.html")

def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})