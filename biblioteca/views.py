# Importamos los viewsets de DRF
# Un viewset es como un "controlador" que maneja las solicitudes HTTP (GET, POST, PUT, DELETE)
from rest_framework import viewsets

# Importamos todos nuestros modelos
# Cada modelo representa una tabla en la base de datos
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo

# Importamos los serializers correspondientes a cada modelo
# Los serializers convierten los objetos de la base de datos a JSON y también permiten crear/actualizar objetos desde JSON
from .serializers import (
    NacionalidadSerializer,
    AutorSerializer,
    ComunaSerializer,
    DireccionSerializer,
    BibliotecaSerializer,
    LibroSerializer,
    LectorSerializer,
    PrestamoSerializer
)

# ======================================================
# Cada clase aquí define un ViewSet para un modelo específico
# Un ViewSet es como un "controlador" que define cómo manejar las solicitudes
# ======================================================

# ViewSet para Nacionalidad
class NacionalidadViewSet(viewsets.ModelViewSet):
    # queryset define qué registros vamos a manejar en esta vista
    queryset = Nacionalidad.objects.all()
    # serializer_class define cómo convertir los datos a JSON y validar datos al crear/actualizar
    serializer_class = NacionalidadSerializer

# ViewSet para Autor
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# ViewSet para Comuna
class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

# ViewSet para Direccion
class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

# ViewSet para Biblioteca
class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

# ViewSet para Libro
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# ViewSet para Lector
class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

# ViewSet para Prestamo
class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
