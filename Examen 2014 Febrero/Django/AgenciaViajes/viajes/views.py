from django.shortcuts import render, render_to_response, RequestContext
from viajes.models import *
from django.http import HttpResponseRedirect
from viajes.forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Indice(request):
	usuario = request.user
	return render_to_response('index.html',{'usuario':usuario})


def VerDestinos(request):
	destinos = Destino.objects.all()
	return render_to_response('destinos.html', {'destinos':destinos})
	
def VerDestino(request,destino_id):
	destino = Destino.objects.get(pk=destino_id)
	return render_to_response('destino.html', {'destino':destino})
	
@login_required(login_url='/')
def AddDestino(request):
	if request.method == 'POST':
		destino = Destino()
		formulario = DestinoForm(request.POST, instance = destino)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = DestinoForm()
		
	usuario = request.user	
	return render_to_response('AddDestino.html', {'formulario':formulario, 'usuario':usuario}, context_instance = RequestContext(request))
	
def VerViajes(request):
	viajes = Viaje.objects.all()
	return render_to_response('viajes.html', {'viajes':viajes})
	
def VerViaje(request,viaje_id):
	viaje = Viaje.objects.get(pk=viaje_id)
	return render_to_response('viaje.html', {'viaje':viaje})
	
@login_required(login_url='/')
def AddViaje(request):
	viaje = Viaje()
	if request.method == 'POST':
		formulario = ViajeForm(request.POST, instance = viaje)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ViajeForm()
	return render_to_response('AddViaje.html',{'formulario':formulario},context_instance = RequestContext(request))

@login_required(login_url='/')	
def EditViaje(request,viaje_id):
	viaje = Viaje.objects.get(pk=viaje_id)
	if request.method == 'POST':
		formulario = ViajeForm(request.POST, instance = viaje)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ViajeForm(instance = viaje)
	return render_to_response('EditarViaje.html',{'formulario':formulario},context_instance = RequestContext(request)) 
	
def log(request):	
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		user = request.POST['username']
		passw = request.POST['password']
		access = authenticate(username=user,password=passw)
		if access is not None:
			login(request,access)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')	
	else:
		formulario = AuthenticationForm()
	return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
@login_required(login_url='/login')
def exit(request):
	logout(request)
	return HttpResponseRedirect('/')
	
	

def VerRutas(request):
	rutas = Ruta.objects.all()
	return render_to_response('rutas.html',{'rutas':rutas})
	
@login_required(login_url='/Error')	
def AddRuta(request):
	ruta = Ruta()
	usuario = request.user
	if request.method == 'POST':
		formulario = RutaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = RutaForm()
	return render_to_response('AddRuta.html',{'formulario':formulario, 'usuario':usuario},context_instance=RequestContext(request))
	
def VerRuta(request,ruta_id):
	ruta = Ruta.objects.get(pk=ruta_id)
	return render_to_response('ruta.html',{'ruta':ruta})
	
def EditRuta(request,ruta_id):
	ruta = Ruta.objects.get(pk=ruta_id)
	usuario = request.user
	if request.method == 'POST':
		formulario = RutaForm(request.POST,instance = ruta)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = RutaForm(instance = ruta)
	return render_to_response('AddRuta.html',{'formulario':formulario,'usuario':usuario},context_instance=RequestContext(request))			
				
