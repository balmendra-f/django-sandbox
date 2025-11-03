# /app/views.py
from django.shortcuts import render
from biblioteca.models import Libro
from biblioteca.views import LibroFilter  # si LibroFilter está en views.py de biblioteca

def home_template(request):
    return render(request, "home.html")


def listado_libros(request):
    # aplicamos filtros a todos los libros
    f = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(request, "biblioteca/lista_libros.html", {"filter": f})
