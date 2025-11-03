# /app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from biblioteca.models import Libro
from biblioteca.views import LibroFilter  # si LibroFilter está en views.py de biblioteca

# Home simple
def home_template(request):
    return render(request, "home.html")

# Listado de libros protegido (solo usuarios logueados)
@login_required
def listado_libros(request):
    # aplicamos filtros a todos los libros
    f = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(request, "biblioteca/lista_libros.html", {"filter": f})

# Registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
