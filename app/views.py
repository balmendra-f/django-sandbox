# /app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from biblioteca.models import Libro
from biblioteca.views import LibroFilter
from django.contrib import messages
from django.contrib.auth import login

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
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(
                request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})
