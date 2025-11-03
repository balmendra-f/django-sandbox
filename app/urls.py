# /app/urls.py
from django.contrib import admin
from django.urls import path, include
from app import views  # nuestras vistas
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # App biblioteca
    path('api/', include('biblioteca.urls')),  # URLs de la app biblioteca

    # Home
    path('', views.home_template, name='home'),

    # Listado de libros (login requerido)
    path('libros/', views.listado_libros, name='listado_libros'),

    # Autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]
