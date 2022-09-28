from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre="Desarrollo ", camada= 21000)
    curso.save()
    documentoDeTexto= f"-----> Curso: {curso.nombre}   Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)


    