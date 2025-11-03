from django.contrib import admin
from django.urls import include, path
from app import views  # importamos nuestras vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),  # URLs de la app biblioteca
    path('', views.home_template, name='home'),  # home page
    path('libros/', views.listado_libros, name='listado_libros'),  # listado de libros
]
