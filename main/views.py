from django.shortcuts import render
from forms import FormContacto
# Orden de vista en el menu.


def inicio(request):
	template = "main/inicio.html"
	context = {}
	return render(request, template, context)


# Flotarium
def quienes_somos(request):
	template = "main/quienes_somos.html"
	context = {}
	return render(request, template, context)


def sesion_flotacion(request):
	template = "main/sesion_flotacion.html"
	context = {}
	return render(request, template, context)


def programas(request):
	template = "main/programas.html"
	context = {}
	return render(request, template, context)


def programa(request):
	template = "main/programa.html"
	context = {}
	return render(request, template, context)


# Terapia FloatREST
def vacio_baneficios(request):
	template = "main/vacio_beneficios.html"
	context = {}
	return render(request, template, context)


def efectos_explicacion(request):
	template = "main/efectos_explicacion.html"
	context = {}
	return render(request, template, context)


def historia_actualidad(request):
	template = "main/historia_actualidad.html"
	context = {}
	return render(request, template, context)


def investigacion_cientifica(request):
	template = "main/investigacion_cientifica.html"
	context = {}
	return render(request, template, context)


def contacto(request):
	template = "main/contacto.html"

	if request.method == "POST":
		form_contacto = FormContacto(request.POST)
		if form_contacto.is_valid():
			mensaje = form_contacto.cleaned_data["mensaje"]
			print mensaje
		else:
			pass
	else:
		form_contacto = FormContacto(initial={'nombre_completo': 'Alejo'})

	lista_ejemplo = [True, 'LISTA DE LOS MEJORES SOUNDTRACKS']
	diccionario = {'Matrix': 'Clubbed to Death', 'Fight Club': 'Who is Tyler Durden',
	               'Inception': 'Time'}
	lista_ejemplo.append(diccionario)

	context = {'form_contacto': form_contacto, 'lista_ejemplo': lista_ejemplo}
	return render(request, template, context)
