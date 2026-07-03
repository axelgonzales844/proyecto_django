from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm

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
            return render(request,'registros/contacto.html')
        form = ComentarioContactoForm()
        return render(request,'registro/contacto.html',{'form':form})
    
def contacto(request):
    return render(request,"registros/contacto.html")