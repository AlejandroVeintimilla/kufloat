from django import forms
from django.forms import TextInput, EmailInput, Textarea, NumberInput, Select
from django.forms.extras.widgets import SelectDateWidget


class FormContacto(forms.Form):
	_bandas = [('pink_floyd', 'Pink Floyd'), ('led_z', 'Led Zeppelin'), ('soda', 'Soda Stereo')]

	nombre_completo = forms.CharField(max_length=150, required=False, label="Nombre Completo",
		                              widget=TextInput(attrs={'class': 'form-control',
		                              	'name': 'nombre_completo'}))

	email = forms.EmailField(required=True, widget=EmailInput(attrs={'class': 'form-control'}))

	mensaje = forms.CharField(max_length=750, required=True,
		                      widget=Textarea(attrs={'rows': 5, 'class': 'form-control'}))

	fecha = forms.DateField(required=False,
		                    widget=SelectDateWidget(attrs={'class': 'form-control'}))

	edad = forms.IntegerField(required=False, max_value=10, min_value=0,
		                      widget=NumberInput(attrs={'class': 'form-control'}))

	banda_favorita = forms.ChoiceField(required=False, choices=_bandas,
		                      widget=Select(attrs={'class': 'form-control'}))
