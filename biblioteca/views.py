from rest_framework import viewsets
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Nacionalidad,
    Autor,
    Comuna,
    Direccion,
    Biblioteca,
    Libro,
    Lector,
    Prestamo,
    Categoria
)
from .serializers import (
    NacionalidadSerializer,
    AutorSerializer,
    ComunaSerializer,
    DireccionSerializer,
    BibliotecaSerializer,
    LibroSerializer,
    LectorSerializer,
    PrestamoSerializer,
    CategoriaSerializer
)

# ---------------------------
# FILTROS
# ---------------------------

class LibroFilter(django_filters.FilterSet):
    id_categoria = django_filters.ModelChoiceFilter(queryset=Categoria.objects.all())
    id_autor = django_filters.ModelChoiceFilter(queryset=Autor.objects.all())

    class Meta:
        model = Libro
        fields = ['id_categoria', 'id_autor', 'habilitado']


class PrestamoFilter(django_filters.FilterSet):
    id_libro = django_filters.ModelChoiceFilter(queryset=Libro.objects.all())
    id_lector = django_filters.ModelChoiceFilter(queryset=Lector.objects.all())
    fecha_prestamo = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Prestamo
        fields = ['id_libro', 'id_lector', 'fecha_prestamo']


class LectorFilter(django_filters.FilterSet):
    id_biblioteca = django_filters.ModelChoiceFilter(queryset=Biblioteca.objects.all())
    habilitado = django_filters.BooleanFilter()

    class Meta:
        model = Lector
        fields = ['id_biblioteca', 'habilitado']


# ---------------------------
# VIEWSETS
# ---------------------------

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pais', 'nacionalidad']


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_nacionalidad', 'nombre', 'bio']


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo']


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_comuna', 'calle', 'numero', 'departamento']


class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'id_direccion']


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LibroFilter


class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LectorFilter


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PrestamoFilter
