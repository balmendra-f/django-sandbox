from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo, Categoria
)
from .serializers import (
    NacionalidadSerializer, AutorSerializer, ComunaSerializer, DireccionSerializer,
    BibliotecaSerializer, LibroSerializer, LectorSerializer, PrestamoSerializer, CategoriaSerializer
)

class NacionalidadFilter(django_filters.FilterSet):
    pais = django_filters.CharFilter(lookup_expr='icontains')
    nacionalidad = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Nacionalidad
        fields = ['pais', 'nacionalidad']


class AutorFilter(django_filters.FilterSet):
    id_nacionalidad = django_filters.ModelChoiceFilter(queryset=Nacionalidad.objects.all())
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    bio = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Autor
        fields = ['id_nacionalidad', 'nombre', 'bio']


class ComunaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    codigo = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Comuna
        fields = ['nombre', 'codigo']


class DireccionFilter(django_filters.FilterSet):
    id_comuna = django_filters.ModelChoiceFilter(queryset=Comuna.objects.all())
    calle = django_filters.CharFilter(lookup_expr='icontains')
    numero = django_filters.CharFilter(lookup_expr='icontains')
    departamento = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Direccion
        fields = ['id_comuna', 'calle', 'numero', 'departamento']


class BibliotecaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    id_direccion = django_filters.ModelChoiceFilter(queryset=Direccion.objects.all())

    class Meta:
        model = Biblioteca
        fields = ['nombre', 'id_direccion']


class CategoriaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nombre']


class LibroFilter(django_filters.FilterSet):
    id_categoria = django_filters.ModelChoiceFilter(queryset=Categoria.objects.all())
    id_autor = django_filters.ModelChoiceFilter(queryset=Autor.objects.all())
    habilitado = django_filters.BooleanFilter()

    class Meta:
        model = Libro
        fields = ['id_categoria', 'id_autor', 'habilitado']


class LectorFilter(django_filters.FilterSet):
    id_biblioteca = django_filters.ModelChoiceFilter(queryset=Biblioteca.objects.all())
    habilitado = django_filters.BooleanFilter()

    class Meta:
        model = Lector
        fields = ['id_biblioteca', 'habilitado']


class PrestamoFilter(django_filters.FilterSet):
    id_libro = django_filters.ModelChoiceFilter(queryset=Libro.objects.all())
    id_lector = django_filters.ModelChoiceFilter(queryset=Lector.objects.all())
    fecha_prestamo = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Prestamo
        fields = ['id_libro', 'id_lector', 'fecha_prestamo']



class AuthenticatedModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]



class NacionalidadViewSet(AuthenticatedModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NacionalidadFilter


class AutorViewSet(AuthenticatedModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AutorFilter


class ComunaViewSet(AuthenticatedModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComunaFilter


class DireccionViewSet(AuthenticatedModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DireccionFilter


class BibliotecaViewSet(AuthenticatedModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BibliotecaFilter


class CategoriaViewSet(AuthenticatedModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoriaFilter


class LibroViewSet(AuthenticatedModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LibroFilter


class LectorViewSet(AuthenticatedModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LectorFilter


class PrestamoViewSet(AuthenticatedModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PrestamoFilter
