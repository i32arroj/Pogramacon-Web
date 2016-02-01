from django.forms import ModelForm
from django import forms
from viajes.models import *

class DestinoForm(forms.ModelForm):
	class Meta:
		model = Destino
		
class ViajeForm(forms.ModelForm):
	class Meta:
		model = Viaje
		
class RutaForm(forms.ModelForm):
	class Meta:
		model = Ruta		
