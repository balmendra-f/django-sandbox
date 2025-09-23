from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo
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

class NacionalidadViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Nacionalidad.objects.all()
        serializer = NacionalidadSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NacionalidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Nacionalidad.objects.all()
        nacionalidad = get_object_or_404(queryset, pk=pk)
        serializer = NacionalidadSerializer(nacionalidad)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Nacionalidad.objects.all()
        nacionalidad = get_object_or_404(queryset, pk=pk)
        serializer = NacionalidadSerializer(nacionalidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Nacionalidad.objects.all()
        nacionalidad = get_object_or_404(queryset, pk=pk)
        nacionalidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AutorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Autor.objects.all()
        autor = get_object_or_404(queryset, pk=pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Autor.objects.all()
        autor = get_object_or_404(queryset, pk=pk)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Autor.objects.all()
        autor = get_object_or_404(queryset, pk=pk)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComunaViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comuna.objects.all()
        serializer = ComunaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ComunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Comuna.objects.all()
        comuna = get_object_or_404(queryset, pk=pk)
        serializer = ComunaSerializer(comuna)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Comuna.objects.all()
        comuna = get_object_or_404(queryset, pk=pk)
        serializer = ComunaSerializer(comuna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Comuna.objects.all()
        comuna = get_object_or_404(queryset, pk=pk)
        comuna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DireccionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Direccion.objects.all()
        serializer = DireccionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DireccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Direccion.objects.all()
        direccion = get_object_or_404(queryset, pk=pk)
        serializer = DireccionSerializer(direccion)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Direccion.objects.all()
        direccion = get_object_or_404(queryset, pk=pk)
        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Direccion.objects.all()
        direccion = get_object_or_404(queryset, pk=pk)
        direccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BibliotecaViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Biblioteca.objects.all()
        serializer = BibliotecaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BibliotecaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Biblioteca.objects.all()
        biblioteca = get_object_or_404(queryset, pk=pk)
        serializer = BibliotecaSerializer(biblioteca)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Biblioteca.objects.all()
        biblioteca = get_object_or_404(queryset, pk=pk)
        serializer = BibliotecaSerializer(biblioteca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Biblioteca.objects.all()
        biblioteca = get_object_or_404(queryset, pk=pk)
        biblioteca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LibroViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Libro.objects.all()
        serializer = LibroSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Libro.objects.all()
        libro = get_object_or_404(queryset, pk=pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Libro.objects.all()
        libro = get_object_or_404(queryset, pk=pk)
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Libro.objects.all()
        libro = get_object_or_404(queryset, pk=pk)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LectorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Lector.objects.all()
        serializer = LectorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Lector.objects.all()
        lector = get_object_or_404(queryset, pk=pk)
        serializer = LectorSerializer(lector)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Lector.objects.all()
        lector = get_object_or_404(queryset, pk=pk)
        serializer = LectorSerializer(lector, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Lector.objects.all()
        lector = get_object_or_404(queryset, pk=pk)
        lector.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PrestamoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Prestamo.objects.all()
        serializer = PrestamoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Prestamo.objects.all()
        prestamo = get_object_or_404(queryset, pk=pk)
        serializer = PrestamoSerializer(prestamo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Prestamo.objects.all()
        prestamo = get_object_or_404(queryset, pk=pk)
        serializer = PrestamoSerializer(prestamo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Prestamo.objects.all()
        prestamo = get_object_or_404(queryset, pk=pk)
        prestamo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
