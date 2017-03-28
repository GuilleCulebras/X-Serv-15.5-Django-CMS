from django.shortcuts import render
from models import Pages
from django.http import HttpResponse


# Create your views here.

def searchContent(request, name):
	try:
		page = Pages.objects.get(name=name)
		respuesta = page.page
	except Pages.DoesNotExist:
		respuesta = "No existe"
	return HttpResponse(respuesta)

def createPage(request, name, page):
	newPage = Pages(name=name,page=page)
	newPage.save()

	return HttpResponse(newPage.name + " guardada")

def barra(request):
	pages = Pages.objects.all()
	respuesta = ""
	for page in pages:
		respuesta += page.name + " : " + page.page + "<br>"
	return HttpResponse(respuesta)

def error(request):
	return HttpResponse("404 Not Found")