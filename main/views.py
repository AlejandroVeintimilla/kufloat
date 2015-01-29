from django.shortcuts import render

# Create your views here.

def inicio(request):
	template = "main/inicio.html"
	context = {}
	return render(request, template, context)

def quienes_somos(request):
	template = "main/quienes_somos.html"
	context = {}
	return render(request, template, context)

def historia_actualidad(request):
	template = "main/historia_actualidad.html"
	context = {}
	return render(request, template, context)

def efectos_explicacion(request):
	template = "main/efectos_explicacion.html"
	context = {}
	return render(request, template, context)

def e_explicacion(request):
	template =  "main/e_explicacion.html"
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

def contacto(request):
	template = "main/contacto.html"
	context = {}
	return render(request, template, context)