from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from biblioteca.models import Libro
from biblioteca.views import LibroFilter
from django.contrib import messages
from django.contrib.auth import login

def home_template(request):
    return render(request, "home.html")

@login_required
def listado_libros(request):
    f = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(request, "biblioteca/lista_libros.html", {"filter": f})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # --- DIAGNÓSTICO DE LA SESIÓN ---
            print("Contenido de la sesión después del login:")
            for key, value in request.session.items():
                print(f"{key}: {value}")
            # --------------------------------

            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(
                request,
                "No ha sido posible Registrarlo. Por favor revise el formulario por errores."
            )
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})
