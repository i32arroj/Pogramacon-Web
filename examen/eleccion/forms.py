from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from eleccion.models import *
from django.contrib.auth.forms import UserCreationForm

class circunscritoForm(forms.ModelForm):
    class Meta:
        model=Circunscrito
        fields=['nombre','escanyos']

class MesaForm(ModelForm):
	class Meta:
		model=Mesa

def usuarioLogin(request):
    if request.method=='POST':
        formulario=autenticacionForm(request.POST)
        if formulario.is_valid:
            usuario=request.POST['username']
            clave=request.POST['password']
            acceso=authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect('/')
                else:
                    return render(request, 'errorLogin.html')
            else:
                return render(request, 'errorLogin.html')
    else:
        formulario=autenticacionForm()
    contexto={'formulario':formulario}
    return render(request,'login.html',contexto)

