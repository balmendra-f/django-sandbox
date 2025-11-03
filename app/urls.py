from django.contrib import admin
from django.urls import path, include
from app import views  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')), 
    path('', views.home_template, name='home'),
    path('libros/', views.listado_libros, name='listado_libros'),

    # Autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]
