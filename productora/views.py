from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from .forms import Formularios
from .models import Banda, Tomnk

# Create your views here.

def home(request):
	band = Banda.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'banda': band
	}
	return HttpResponse(template.render(context, request))

def history(request):
	band = Banda.objects.order_by('id')
	integrantes = Tomnk.objects.order_by('id')
	template = loader.get_template('history.html')
	context = {
		'banda': band,
		'tomnk': integrantes,
	}
	return HttpResponse(template.render(context, request))

def contact(request):
	if request.method == "POST":
		form = Formularios(request.POST)
		if form.is_valid():
			nombre = request.POST.get('nombre')
			apellido = request.POST.get('apellido')
			mensaje = request.POST.get('mensaje')
			from_email = request.POST.get('email')
			data = form.cleaned_data
			send_mail("Me llamo " + nombre + " " + apellido, "Correo electronico: " + from_email + "\n" + "Mensaje enviado: " + "\n" + mensaje , "produccionestomnk@gmail.com", ['produccionestomnk@gmail.com'])
			# send_mail(
			# 	data['nombre'] + " " + data['apellido'],
			# 	"mensaje de: " + data["email"] + "\n" + data['mensaje'],
			# 	"fotosdiarias30@gmail.com",
			# 	["dende149@gmail.com"],
			# )
			
			return HttpResponseRedirect('/')
	else:
		formulario = Formularios()

	template = loader.get_template('contact.html')
	context = {
		'formulario': formulario
	}
	return HttpResponse(template.render(context, request))

def info_bandas(request, pk):
	banda = get_object_or_404(Banda, pk=pk)
	template = loader.get_template('info_bandas.html')
	context = {
		'banda': banda
	}
	return HttpResponse(template.render(context, request))

def pictures(request):
	banda = Banda.objects.order_by('id')
	template = loader.get_template('pictures.html')
	context = {
		'banda': banda
	}
	return HttpResponse(template.render(context, request))
